# 개발 환경 설정 (config.ini를 src/로 복사)
dev-setup:
    @echo "Setting up development environment..."
    cp config.ini src/config.ini
    @echo "Copied config.ini to src/config.ini"

# Pyxel Web 버전 실행
# 웹 브라우저에서 게임을 실행합니다
web:
    @echo "Starting Pyxel Web server..."
    @echo "Open http://localhost:8000 in your web browser"
    @echo "Press Ctrl+C to stop the server"
    @echo ""
    python3 -m http.server 8000

# Pyxel 앱을 패키징하여 .pyxapp 파일 생성
package:
    @echo "Packaging Pyxel app..."
    # Copy config.ini from project root to src/ for packaging
    cp config.ini src/config.ini
    python3 -m pyxel package src src/main.py
    rm -f src/config.ini
    @echo "Created src.pyxapp"

# Pyxel 앱을 단일 HTML 파일로 변환 (로드 시간 최적화)
# 참고 정보:
# - Pyxel cli.py의 create_html_from_pyxel_app 함수 (line 425-445)
#   - app2html 명령이 launchPyxel 함수를 호출하는 HTML 생성
#   - 기본 형식: launchPyxel({ command: "play", name: "...", gamepad: "enabled", base64: "..." })
# - 이전 index.html에서 pyxel-run 태그에 packages="numpy" 추가 경험
# - Pyodide에서 numpy 패키지를 로드하기 위해 packages 파라미터 필요
# - cli.py는 packages 파라미터를 지원하지 않으므로 생성된 HTML을 후처리하여 추가
build:
    @echo "Building web version..."
    # Copy config.ini from project root to src/ for packaging
    cp config.ini src/config.ini
    python3 -m pyxel package src src/main.py
    python3 -m pyxel app2html src.pyxapp
    python3 -c "import re; content = open('src.html', 'r').read(); content = re.sub(r'launchPyxel\(\{ command: \"play\", name: \"([^\"]+)\", gamepad: \"enabled\", base64: \"([^\"]+)\" \}\)', r'launchPyxel({ command: \"play\", name: \"\1\", gamepad: \"enabled\", packages: \"numpy,pydantic\", base64: \"\2\" })', content); open('index.html', 'w').write(content)"
    rm -f src.html src.pyxapp src/config.ini
    @echo "Created index.html - optimized single-file web version with numpy"

