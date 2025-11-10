# Pyxel Web 버전 실행
# 웹 브라우저에서 게임을 실행합니다
web:
    @echo "Starting Pyxel Web server..."
    @echo "Open http://localhost:8000 in your web browser"
    @echo "Press Ctrl+C to stop the server"
    @echo ""
    python3 -m http.server 8000

