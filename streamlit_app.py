import streamlit as st

# 1. 웹 페이지 제목 및 설명 설정
st.title("🔤 알파벳 빈칸 맞추기 퀴즈!")
st.write("단어의 빈칸(`_`)에 들어갈 알맞은 알파벳을 입력해 보세요.")

# 2. 문제 데이터 설정 (원본 로직 유지)
words = ["bana__", "socc__", "happ_"]
answers = ["na", "er", "y"]

# 3. 사이드바 또는 메인 화면에서 문제 선택하기 (range 활용)
st.subheader("📝 문제를 선택하세요")
problem_index = st.selectbox(
    "풀고 싶은 단어를 선택하세요:",
    range(len(words)),
    format_func=lambda x: f"문제 {x+1}: {words[x]}",
)

# 선택된 문제 표시
current_word = words[problem_index]
correct_answer = answers[problem_index]

st.info(f"현재 제시된 단어: **{current_word}**")

# 4. 사용자 입력 위젯 (input 대신 st.text_input 사용)
user_input = st.text_input("빈칸에 들어갈 알파벳을 입력하세요:", key=f"input_{problem_index}").strip().lower()

# 5. 정답 확인 로직 (print 대신 st.success, st.error 사용)
if st.button("정답 확인하기", type="primary"):
    if user_input == correct_answer:
        st.success(f"🎉 정답입니다! 완성된 단어: **{current_word.replace('__', correct_answer).replace('_', correct_answer)}**")
        st.balloons()  # 축하 효과
    else:
        st.error("❌ 아쉽습니다! 다시 한번 생각해 보세요.")