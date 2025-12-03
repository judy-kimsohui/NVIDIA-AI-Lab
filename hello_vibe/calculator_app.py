import streamlit as st

# 페이지 설정
st.set_page_config(page_title="계산기", page_icon="🔢", layout="centered")

# CSS 스타일 추가
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 70px;
        font-size: 28px;
        font-weight: bold;
        border-radius: 10px;
        margin: 2px;
        padding: 10px;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        transition: 0.2s;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'first_num' not in st.session_state:
    st.session_state.first_num = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'new_number' not in st.session_state:
    st.session_state.new_number = True

# 콜백 함수 정의
def click_number(num):
    if st.session_state.new_number:
        st.session_state.display = str(num)
        st.session_state.new_number = False
    else:
        if st.session_state.display == "0":
            st.session_state.display = str(num)
        else:
            st.session_state.display += str(num)

def click_decimal():
    if st.session_state.new_number:
        st.session_state.display = "0."
        st.session_state.new_number = False
    elif "." not in st.session_state.display:
        st.session_state.display += "."

def click_operation(op):
    if st.session_state.display != "Error":
        st.session_state.first_num = float(st.session_state.display)
        st.session_state.operation = op
        st.session_state.new_number = True

def click_equal():
    if st.session_state.first_num is not None and st.session_state.operation is not None:
        try:
            second_num = float(st.session_state.display)
            
            if st.session_state.operation == "+":
                result = st.session_state.first_num + second_num
            elif st.session_state.operation == "-":
                result = st.session_state.first_num - second_num
            elif st.session_state.operation == "*":
                result = st.session_state.first_num * second_num
            elif st.session_state.operation == "/":
                if second_num == 0:
                    st.session_state.display = "Error"
                    st.session_state.first_num = None
                    st.session_state.operation = None
                    st.session_state.new_number = True
                    return
                result = st.session_state.first_num / second_num
            
            # 결과가 정수면 정수로 표시
            if result == int(result):
                st.session_state.display = str(int(result))
            else:
                st.session_state.display = str(round(result, 8))
            
            st.session_state.first_num = None
            st.session_state.operation = None
            st.session_state.new_number = True
        except:
            st.session_state.display = "Error"
            st.session_state.first_num = None
            st.session_state.operation = None
            st.session_state.new_number = True

def click_clear():
    st.session_state.display = "0"
    st.session_state.first_num = None
    st.session_state.operation = None
    st.session_state.new_number = True

# UI
st.title("🔢 계산기")

# 디스플레이
st.markdown(f"""
<div style='background-color: #1e1e1e; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h1 style='color: white; text-align: right; margin: 0; font-size: 48px;'>{st.session_state.display}</h1>
</div>
""", unsafe_allow_html=True)

# 버튼 레이아웃
# 첫 번째 줄: C, +, -, *
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("C", key="clear", on_click=click_clear)

with col2:
    st.button("➕", key="add", on_click=click_operation, args=("+",))

with col3:
    st.button("➖", key="sub", on_click=click_operation, args=("-",))

with col4:
    st.button("✖️", key="mul", on_click=click_operation, args=("*",))

# 두 번째 줄: 7, 8, 9, /
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("7", key="7", on_click=click_number, args=(7,))

with col2:
    st.button("8", key="8", on_click=click_number, args=(8,))

with col3:
    st.button("9", key="9", on_click=click_number, args=(9,))

with col4:
    st.button("➗", key="div", on_click=click_operation, args=("/",))

# 세 번째 줄: 4, 5, 6
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("4", key="4", on_click=click_number, args=(4,))

with col2:
    st.button("5", key="5", on_click=click_number, args=(5,))

with col3:
    st.button("6", key="6", on_click=click_number, args=(6,))

with col4:
    st.write("")

# 네 번째 줄: 1, 2, 3
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("1", key="1", on_click=click_number, args=(1,))

with col2:
    st.button("2", key="2", on_click=click_number, args=(2,))

with col3:
    st.button("3", key="3", on_click=click_number, args=(3,))

with col4:
    st.write("")

# 다섯 번째 줄: 0, ., =
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("0", key="0", on_click=click_number, args=(0,))

with col2:
    st.button(".", key="dot", on_click=click_decimal)

with col3:
    st.write("")

with col4:
    st.button("=", key="equal", on_click=click_equal)

# 사이드바
st.sidebar.header("📌 정보")
st.sidebar.info("버튼을 클릭하여 계산하세요!")
st.sidebar.write("**기능:**")
st.sidebar.write("- 사칙연산 (+, -, *, /)")
st.sidebar.write("- 소수점 계산")
st.sidebar.write("- C: 초기화")
st.sidebar.write("")
st.sidebar.write("**사용법:**")
st.sidebar.write("1. 숫자 버튼 클릭")
st.sidebar.write("2. 연산자 버튼 클릭")
st.sidebar.write("3. 숫자 버튼 클릭")
st.sidebar.write("4. = 버튼 클릭")
st.sidebar.write("")
st.sidebar.write("**예시:**")
st.sidebar.write("5 ➕ 3 = 8")
st.sidebar.write("10 ➖ 4 = 6")
st.sidebar.write("6 ✖️ 7 = 42")
st.sidebar.write("15 ➗ 3 = 5")
