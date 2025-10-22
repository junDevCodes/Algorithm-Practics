```bash
cp ~/.bashrc ~/.bashrc.backup.$(date +%Y%m%d_%H%M%S)

cat >> ~/.bashrc << 'SHELL_FUNCTIONS_EOF'

al ()
{
    if [ $# -eq 0 ]; then
        echo "❗️사용법: al <사이트> <문제번호>";
        echo "";
        echo "📋 지원 사이트:";
        echo "  s  → SWEA (Samsung SW Expert Academy)";
        echo "  b  → BOJ (Baekjoon Online Judge)";
        echo "  p  → Programmers";
        echo "";
        echo "💡 사용 예제:";
        echo "  al s 1234    # SWEA 1234번 문제";
        echo "  al b 10950   # BOJ 10950번 문제";
        echo "  al p 42576   # 프로그래머스 42576번 문제";
        return 1;
    fi;
    if [ $# -eq 1 ]; then
        case "$1" in
            s | b | p | swea | boj | programmers)
                echo "❗️문제번호가 누락되었습니다!";
                echo "올바른 형식: al $1 <문제번호>";
                echo "예시: al $1 1000"
            ;;
            *)
                echo "❗️사이트 코드가 누락되었거나 잘못되었습니다!";
                echo "입력하신 값: '$1'";
                echo "📋 올바른 사이트 코드: s, b, p";
                echo "예시: al b $1 (BOJ $1번 문제)"
            ;;
        esac;
        return 1;
    fi;
    local site_code="$1";
    local problem="$2";
    local base_dir="";
    if [ -d "$HOME/Desktop/Algorithm-Practics" ]; then
        base_dir="$HOME/Desktop/Algorithm-Practics";
        echo "🏢 회사 환경 감지";
    else
        if [ -d "$HOME/Desktop/workspace/algorithms" ]; then
            base_dir="$HOME/Desktop/workspace/algorithms";
            echo "🏠 집 환경 감지";
        else
            echo "📁 알고리즘 디렉토리 생성 중...";
            echo "1) ~/Desktop/Algorithm-Practics/ (회사 스타일)";
            echo "2) ~/Desktop/workspace/algorithms/ (집 스타일)";
            read -p "선택 (1-2): " -n 1 -r choice;
            echo;
            case "$choice" in
                1)
                    base_dir="$HOME/Desktop/Algorithm-Practics"
                ;;
                2)
                    base_dir="$HOME/Desktop/workspace/algorithms"
                ;;
                *)
                    base_dir="$HOME/Desktop/Algorithm-Practics"
                ;;
            esac;
            mkdir -p "$base_dir";
            echo "✅ 디렉토리 생성: $base_dir";
        fi;
    fi;
    case "$site_code" in
        s | swea)
            local site_name="swea";
            local file_prefix="swea";
            local site_display="SWEA"
        ;;
        b | boj)
            local site_name="boj";
            local file_prefix="boj";
            local site_display="BOJ"
        ;;
        p | programmers)
            local site_name="programmers";
            local file_prefix="programmers";
            local site_display="Programmers"
        ;;
        *)
            echo "❗️지원하지 않는 사이트 코드: '$site_code'";
            return 1
        ;;
    esac;
    if ! [[ "$problem" =~ ^[0-9]+$ ]]; then
        echo "❗️문제번호는 숫자여야 합니다: '$problem'";
        return 1;
    fi;
    local dir="$base_dir/$site_name/$problem";
    local file="$dir/${file_prefix}_${problem}.py";
    local editor=$(get_active_ide);
    echo "🎯 사이트: $site_display";
    echo "📝 문제번호: $problem";
    echo "📌 감지된 IDE: $editor";
    mkdir -p "$dir";
    if [ ! -f "$file" ]; then
        echo "🆕 새 문제 파일 생성 중...";
        cat > "$file" <<PYCODE
# $site_display $problem 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]


[입력]


[출력]


[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""

PYCODE

        case "$site_name" in
            swea)
                cat >> "$file" <<'SWEA_CODE'
T = int(input())

for test_case in range(1, T + 1):
    
    print(f"#{test_case}")
SWEA_CODE

            ;;
            boj)
                cat >> "$file" <<'BOJ_CODE'
N = int(sys.stdin.readline())
# N = int(input())

# 배열 입력
# arr = list(map(int, sys.stdin.readline().split()))

# 여러 줄 입력
# for i in range(N):
#     line = sys.stdin.readline().strip()

# 출력
# print(result)
BOJ_CODE

            ;;
            programmers)
                cat >> "$file" <<'PROG_CODE'
def solution(param):
    """
    프로그래머스 솔루션 함수
    """
    return param

# 테스트
if __name__ == "__main__":
    test_cases = [
        # (입력, 예상출력)
    ]

    for i, (inp, expected) in enumerate(test_cases):
        result = solution(inp)
        print(f"Test {i+1}: {'✅' if result == expected else '❌'}")
PROG_CODE

            ;;
        esac
        echo "✅ 파일 생성 완료!";
    else
        echo "📄 기존 파일 발견! Git 작업을 진행합니다.";
        local git_root="";
        local current_dir="$dir";
        while [ "$current_dir" != "/" ] && [ "$current_dir" != "$HOME" ]; do
            if [ -d "$current_dir/.git" ]; then
                git_root="$current_dir";
                break;
            fi;
            current_dir=$(dirname "$current_dir");
        done;
        if [ -n "$git_root" ]; then
            cd "$git_root";
            local relative_path=$(realpath --relative-to="$git_root" "$dir" 2> /dev/null || python3 -c "import os.path; print(os.path.relpath('$dir', '$git_root'))");
            echo "✅ Git 저장소: $git_root";
            echo "📁 대상: $relative_path";
            git add "$relative_path";
            git commit -m "solve: ${file_prefix}_${problem}" 2> /dev/null && echo "✅ 커밋 완료";
            if git push origin main 2> /dev/null || git push origin master 2> /dev/null; then
                echo "✅ 푸시 완료!";
            else
                echo "⚠️ 푸시 실패 (원격 저장소 확인 필요)";
            fi;
        else
            echo "⚠️ Git 저장소를 찾을 수 없습니다";
        fi;
    fi;
    echo "🎉 $editor에서 파일을 여는 중...";
    case "$editor" in
        pycharm64.exe | pycharm)
            if command -v pycharm64.exe > /dev/null 2>&1; then
                pycharm64.exe "$file" &
            else
                if command -v pycharm > /dev/null 2>&1; then
                    pycharm "$file" &
                else
                    echo "⚠️ PyCharm 실행 파일을 찾을 수 없습니다";
                    code "$file" 2> /dev/null || echo "❌ 파일 열기 실패";
                fi;
            fi
        ;;
        idea64.exe | idea)
            if command -v idea64.exe > /dev/null 2>&1; then
                idea64.exe "$file" &
            else
                if command -v idea > /dev/null 2>&1; then
                    idea "$file" &
                else
                    echo "⚠️ IntelliJ 실행 파일을 찾을 수 없습니다";
                    code "$file" 2> /dev/null || echo "❌ 파일 열기 실패";
                fi;
            fi
        ;;
        *)
            if command -v "$editor" > /dev/null 2>&1; then
                "$editor" "$file" &
            else
                echo "⚠️ $editor를 찾을 수 없습니다. 기본 에디터로 시도...";
                code "$file" 2> /dev/null || subl "$file" 2> /dev/null || echo "❌ 파일 열기 실패";
            fi
        ;;
    esac
}

check_ide ()
{
    echo "🔍 IDE 감지 디버깅 정보:";
    echo "";
    echo "💻 운영체제: $OSTYPE";
    echo "📁 현재 위치: $(pwd)";
    echo "";
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]] || command -v powershell.exe > /dev/null 2>&1; then
        echo "1️⃣ Windows - 실행 중인 IDE 프로세스:";
        local processes=$(powershell.exe -Command "Get-Process | Where-Object {\$_.ProcessName -like '*pycharm*' -or \$_.ProcessName -like '*code*' -or \$_.ProcessName -like '*idea*'} | Select-Object ProcessName, Id" 2> /dev/null | tr -d '\r');
        if [ -n "$processes" ]; then
            echo "$processes";
        else
            echo "   ❌ IDE 프로세스를 찾을 수 없습니다";
        fi;
        echo "";
        echo "2️⃣ 현재 활성 창:";
        local window_title=$(powershell.exe -Command "
            Add-Type @'
using System;
using System.Runtime.InteropServices;
public class User32 {
    [DllImport(\"user32.dll\")]
    public static extern IntPtr GetForegroundWindow();
    [DllImport(\"user32.dll\")]
    public static extern int GetWindowText(IntPtr hWnd, System.Text.StringBuilder text, int count);
}
'@;
\$hwnd = [User32]::GetForegroundWindow();
\$buf = New-Object System.Text.StringBuilder 512;
[void][User32]::GetWindowText(\$hwnd, \$buf, \$buf.Capacity);
Write-Output \$buf.ToString();" 2> /dev/null | tr -d '\r');
        echo "   제목: '$window_title'";
    else
        if [[ "$OSTYPE" == "darwin"* ]]; then
            echo "1️⃣ macOS - 실행 중인 IDE:";
            ps aux | grep -E "(PyCharm|IntelliJ|Visual Studio Code|Sublime)" | grep -v grep || echo "   ❌ IDE를 찾을 수 없습니다";
            echo "";
            echo "2️⃣ 현재 활성 애플리케이션:";
            local active_app=$(osascript -e 'tell application "System Events" to get name of first application process whose frontmost is true' 2> /dev/null);
            echo "   '$active_app'";
        else
            echo "1️⃣ Linux - 실행 중인 IDE:";
            ps aux | grep -E "(pycharm|idea|code|subl)" | grep -v grep || echo "   ❌ IDE를 찾을 수 없습니다";
        fi;
    fi;
    echo "";
    echo "3️⃣ get_active_ide() 결과:";
    local detected_ide=$(get_active_ide);
    echo "   감지된 IDE: '$detected_ide'";
    echo "";
    echo "💡 지원하는 IDE:";
    echo "   • PyCharm (Community/Professional)";
    echo "   • IntelliJ IDEA";
    echo "   • Visual Studio Code";
    echo "   • Sublime Text"
}

get_active_ide ()
{
    local os_type="";
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]] || command -v powershell.exe > /dev/null 2>&1; then
        os_type="windows";
    else
        if [[ "$OSTYPE" == "darwin"* ]]; then
            os_type="mac";
        else
            if [[ "$OSTYPE" == "linux-gnu"* ]]; then
                os_type="linux";
            fi;
        fi;
    fi;
    case "$os_type" in
        "windows")
            local running_processes=$(powershell.exe -Command "Get-Process | Where-Object {\$_.ProcessName -like '*pycharm*' -or \$_.ProcessName -like '*code*' -or \$_.ProcessName -like '*idea*'} | Select-Object ProcessName" 2> /dev/null | tr -d '\r');
            if echo "$running_processes" | grep -iq "pycharm"; then
                echo "pycharm64.exe";
                return;
            else
                if echo "$running_processes" | grep -iq "idea"; then
                    echo "idea64.exe";
                    return;
                else
                    if echo "$running_processes" | grep -iq "code"; then
                        echo "code";
                        return;
                    fi;
                fi;
            fi;
            local window_info=$(powershell.exe -Command "
                Add-Type @'
using System;
using System.Runtime.InteropServices;
public class User32 {
    [DllImport(\"user32.dll\")]
    public static extern IntPtr GetForegroundWindow();
    [DllImport(\"user32.dll\")]
    public static extern int GetWindowText(IntPtr hWnd, System.Text.StringBuilder text, int count);
}
'@;
\$hwnd = [User32]::GetForegroundWindow();
\$buf = New-Object System.Text.StringBuilder 512;
[void][User32]::GetWindowText(\$hwnd, \$buf, \$buf.Capacity);
Write-Output \$buf.ToString();" 2> /dev/null | tr -d '\r');
            if echo "$window_info" | grep -iq "PyCharm"; then
                echo "pycharm64.exe";
            else
                if echo "$window_info" | grep -iq "IntelliJ\|IDEA"; then
                    echo "idea64.exe";
                else
                    if echo "$window_info" | grep -iq "Visual Studio Code"; then
                        echo "code";
                    else
                        echo "code";
                    fi;
                fi;
            fi
        ;;
        "mac")
            local active_app=$(osascript -e 'tell application "System Events" to get name of first application process whose frontmost is true' 2> /dev/null);
            case "$active_app" in
                *PyCharm*)
                    echo "pycharm"
                ;;
                *IntelliJ*)
                    echo "idea"
                ;;
                *"Visual Studio Code"*)
                    echo "code"
                ;;
                *Sublime*)
                    echo "subl"
                ;;
                *)
                    if pgrep -f "PyCharm" > /dev/null; then
                        echo "pycharm";
                    else
                        if pgrep -f "IntelliJ" > /dev/null; then
                            echo "idea";
                        else
                            if pgrep -f "Visual Studio Code" > /dev/null; then
                                echo "code";
                            else
                                if pgrep -f "Sublime" > /dev/null; then
                                    echo "subl";
                                else
                                    echo "code";
                                fi;
                            fi;
                        fi;
                    fi
                ;;
            esac
        ;;
        "linux")
            if pgrep -f "pycharm" > /dev/null; then
                echo "pycharm.sh";
            else
                if pgrep -f "idea" > /dev/null; then
                    echo "idea.sh";
                else
                    if pgrep -f "code" > /dev/null; then
                        echo "code";
                    else
                        if pgrep -f "subl" > /dev/null; then
                            echo "subl";
                        else
                            echo "code";
                        fi;
                    fi;
                fi;
            fi
        ;;
        *)
            echo "code"
        ;;
    esac
}

gitdown ()
{
    echo "🔍 현재 Git 상태:";
    git status --short;
    echo "";
    echo "📝 모든 변경사항을 추가하고 커밋합니다...";
    git add .;
    local commit_msg="";
    local py_file=$(find . -maxdepth 1 -name "*.py" -type f | head -n 1);
    if [ -n "$py_file" ]; then
        local filename=$(basename "$py_file" .py);
        commit_msg="solve: $filename";
    else
        local folder_name=$(basename "$(pwd)");
        commit_msg="update: $folder_name";
    fi;
    echo "📌 커밋 메시지: $commit_msg";
    git commit -m "$commit_msg";
    echo "🌐 원격 저장소로 푸시 중...";
    if git push origin main 2> /dev/null || git push origin master 2> /dev/null; then
        echo "✅ 푸시 완료!";
    else
        echo "⚠️ 푸시 실패";
    fi;
    echo "📁 상위 폴더로 이동";
    cd ..
}

gitup ()
{
    if [ -z "$1" ]; then
        echo "❗️사용법: gitup <git-repository-url>";
        echo "예시: gitup https://github.com/user/repo.git";
        return 1;
    fi;
    echo "🔄 Git 저장소 클론 중: $1";
    git clone "$1" || return 1;
    local repo_name=$(basename "$1" .git);
    echo "📂 $repo_name 폴더로 이동";
    cd "$repo_name" || return;
    local editor=$(get_active_ide);
    echo "📌 감지된 IDE: $editor";
    local target_file="";
    target_file=$(find . -name "*.py" -type f | head -n 1);
    if [ -n "$target_file" ]; then
        echo "🐍 Python 파일 발견: $target_file";
    else
        target_file=$(find . -name "*.html" -type f | head -n 1);
        if [ -n "$target_file" ]; then
            echo "🌐 HTML 파일 발견: $target_file";
        else
            target_file=$(find . -name "README*" -type f | head -n 1);
            if [ -n "$target_file" ]; then
                echo "📄 README 파일 발견: $target_file";
            else
                target_file=$(find . \( -name "*.js" -o -name "*.css" -o -name "*.json" -o -name "*.md" -o -name "*.txt" \) -type f | head -n 1);
                if [ -n "$target_file" ]; then
                    echo "📄 파일 발견: $target_file";
                fi;
            fi;
        fi;
    fi;
    if [ -n "$target_file" ]; then
        echo "🎉 현재 에디터에서 파일 열기: $target_file";
        case "$editor" in
            pycharm64.exe | pycharm)
                if command -v pycharm64.exe > /dev/null 2>&1; then
                    pycharm64.exe "$target_file" &
                else
                    if command -v pycharm > /dev/null 2>&1; then
                        pycharm "$target_file" &
                    else
                        echo "⚠️ PyCharm 실행 파일을 찾을 수 없습니다";
                        code "$target_file" 2> /dev/null || echo "❌ 파일 열기 실패";
                    fi;
                fi
            ;;
            idea64.exe | idea)
                if command -v idea64.exe > /dev/null 2>&1; then
                    idea64.exe "$target_file" &
                else
                    if command -v idea > /dev/null 2>&1; then
                        idea "$target_file" &
                    else
                        echo "⚠️ IntelliJ 실행 파일을 찾을 수 없습니다";
                        code "$target_file" 2> /dev/null || echo "❌ 파일 열기 실패";
                    fi;
                fi
            ;;
            *)
                if command -v "$editor" > /dev/null 2>&1; then
                    "$editor" "$target_file" &
                else
                    echo "⚠️ $editor를 찾을 수 없습니다. 기본 에디터로 시도...";
                    code "$target_file" 2> /dev/null || subl "$target_file" 2> /dev/null || echo "❌ 파일 열기 실패";
                fi
            ;;
        esac;
    else
        echo "⚠️ 적절한 파일을 찾을 수 없습니다";
        echo "📋 클론된 폴더 내용:";
        ls -la;
    fi;
    echo "✅ 프로젝트 준비 완료!"
}

pycharm ()
{
    local target="${1:-.}";
    local pycharm_path="";
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        local possible_paths=("/c/Program Files/JetBrains/PyCharm Community Edition"*/bin/pycharm64.exe "/c/Program Files/JetBrains/PyCharm Professional"*/bin/pycharm64.exe "/c/Users/$USER/AppData/Local/JetBrains/PyCharm Community Edition"*/bin/pycharm64.exe);
        for path in "${possible_paths[@]}";
        do
            if [ -f "$path" ]; then
                pycharm_path="$path";
                break;
            fi;
        done;
    else
        if [[ "$OSTYPE" == "darwin"* ]]; then
            if [ -d "/Applications/PyCharm CE.app" ]; then
                pycharm_path="open -a PyCharm\ CE";
            else
                if [ -d "/Applications/PyCharm.app" ]; then
                    pycharm_path="open -a PyCharm";
                fi;
            fi;
        else
            if command -v pycharm > /dev/null 2>&1; then
                pycharm_path="pycharm";
            else
                if command -v pycharm.sh > /dev/null 2>&1; then
                    pycharm_path="pycharm.sh";
                fi;
            fi;
        fi;
    fi;
    if [ -n "$pycharm_path" ]; then
        echo "🚀 PyCharm 실행: $target";
        $pycharm_path "$target" &
    else
        echo "❌ PyCharm을 찾을 수 없습니다";
        echo "💡 다음 명령어로 IDE를 확인해보세요: check_ide";
    fi
}

SHELL_FUNCTIONS_EOF

source ~/.bashrc

echo "✅ 설치 완료!"
echo "💡 사용법: al s 2105"
```