#!/usr/bin/env python3
"""
AI Titans Thoughtcast — Local macOS Finder Bridge Service
Listens on http://127.0.0.1:8765
Endpoints:
  GET /status -> {"status": "ok", "service": "Finder Bridge"}
  GET /reveal?path=/abs/path/to/file -> runs `open -R <path>`
  GET /open_folder?path=/abs/path/to/dir -> runs `open <dir>`
"""
import sys, os, subprocess, urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8765
PROJECT_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"

class FinderBridgeHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)

        if parsed.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"status":"ok","service":"AI Titans Finder Bridge","port":8765}\n')
            return

        if parsed.path in ('/reveal', '/open'):
            raw_path = qs.get('path', [''])[0].strip()
            if not raw_path:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'{"status":"error","message":"Missing path parameter"}\n')
                return

            # Resolve relative path if needed
            if not raw_path.startswith('/'):
                target_path = os.path.join(PROJECT_ROOT, raw_path)
            else:
                target_path = raw_path

            # If path doesn't exist directly, search by filename or substring in PROJECT_ROOT
            if not os.path.exists(target_path):
                fname = os.path.basename(target_path)
                found = None
                for root, dirs, files in os.walk(PROJECT_ROOT):
                    # Check exact match first
                    if fname in files:
                        found = os.path.join(root, fname)
                        break
                    # Case-insensitive or substring match
                    for f in files:
                        if f.lower() == fname.lower() or (len(fname) >= 6 and fname.lower() in f.lower()):
                            found = os.path.join(root, f)
                            break
                    if found:
                        break
                if found:
                    target_path = found

            if os.path.exists(target_path):
                # reveal in Finder
                subprocess.run(['/usr/bin/open', '-R', target_path])
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                msg = f'{{"status":"ok","revealed":"{target_path}"}}\n'
                self.wfile.write(msg.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                msg = f'{{"status":"error","message":"Path not found on disk","path":"{target_path}"}}\n'
                self.wfile.write(msg.encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        # Quiet logger
        pass

def main():
    server = HTTPServer(('127.0.0.1', PORT), FinderBridgeHandler)
    print(f"Finder Bridge running at http://127.0.0.1:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping Finder Bridge...")
        server.server_close()

if __name__ == '__main__':
    main()
