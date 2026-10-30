
import random
import streamlit as st

st.set_page_config(
    page_title="Quiz Master",
    page_icon="🎯",
    layout="centered"
)

QUESTIONS = [
    {
        "q": "Hành tinh nào gần Mặt Trời nhất?",
        "options": ["Trái Đất", "Sao Kim", "Sao Thủy", "Sao Hỏa"],
        "answer": "Sao Thủy",
        "level": "Dễ"
    },
    {
        "q": "Đại dương lớn nhất thế giới là gì?",
        "options": ["Đại Tây Dương", "Thái Bình Dương",
                    "Ấn Độ Dương", "Bắc Băng Dương"],
        "answer": "Thái Bình Dương",
        "level": "Dễ"
    },
    {
        "q": "Kết quả của 12 × 8 là bao nhiêu?",
        "options": ["86", "96", "108", "92"],
        "answer": "96",
        "level": "Dễ"
    },
    {
        "q": "Nguyên tố hóa học có ký hiệu O là gì?",
        "options": ["Vàng", "Oxy", "Bạc", "Sắt"],
        "answer": "Oxy",
        "level": "Trung bình"
    },
    {
        "q": "Ai là tác giả của Truyện Kiều?",
        "options": ["Nguyễn Du", "Nam Cao",
                    "Tố Hữu", "Xuân Diệu"],
        "answer": "Nguyễn Du",
        "level": "Trung bình"
    },
    {
        "q": "Một byte thường bằng bao nhiêu bit?",
        "options": ["4", "8", "16", "32"],
        "answer": "8",
        "level": "Trung bình"
    },
    {
        "q": "Thủ đô của Nhật Bản là gì?",
        "options": ["Kyoto", "Osaka", "Tokyo", "Nagoya"],
        "answer": "Tokyo",
        "level": "Dễ"
    },
    {
        "q": "Số nguyên tố nhỏ nhất là số nào?",
        "options": ["0", "1", "2", "3"],
        "answer": "2",
        "level": "Khó"
    },
    {
        "q": "Python thường được dùng để làm gì?",
        "options": [
            "Chỉ thiết kế ảnh",
            "Lập trình và phân tích dữ liệu",
            "Chỉ soạn văn bản",
            "Chỉ chỉnh sửa video"
        ],
        "answer": "Lập trình và phân tích dữ liệu",
        "level": "Trung bình"
    },
    {
        "q": "Kết quả của 2 mũ 5 là bao nhiêu?",
        "options": ["10", "16", "25", "32"],
        "answer": "32",
        "level": "Khó"
    }
]

def new_game():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    st.session_state.questions = questions
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.finished = False
    st.session_state.answered = False
    st.session_state.choice = None

if "questions" not in st.session_state:
    new_game()

st.title("🎯 Quiz Master")
st.caption("HÀNH TRÌNH CHINH PHỤC KIẾN THỨC")
st.write("Trả lời 10 câu hỏi để chinh phục thử thách!")

if not st.session_state.finished:
    i = st.session_state.index
    question = st.session_state.questions[i]

    st.progress(i / len(st.session_state.questions))
    st.write(f"🏆 Điểm: {st.session_state.score}")
    st.write(f"📝 Câu {i + 1}/{len(st.session_state.questions)}")
    st.write(f"⭐ Cấp độ: {question['level']}")
    st.subheader(question["q"])

    choice = st.radio(
        "Chọn một đáp án:",
        question["options"],
        index=None,
        key=f"choice_{i}",
        disabled=st.session_state.answered
    )

    if not st.session_state.answered:
        if st.button("✅ Trả lời", use_container_width=True):
            if choice is None:
                st.warning("Bạn hãy chọn một đáp án!")
            else:
                st.session_state.choice = choice
                st.session_state.answered = True

                if choice == question["answer"]:
                    st.session_state.score += 10

                st.rerun()

    if st.session_state.answered:
        if st.session_state.choice == question["answer"]:
            st.success("🎉 Chính xác! +10 điểm")
        else:
            st.error("Chưa chính xác!")
            st.info(f"Đáp án đúng: {question['answer']}")

        if st.button("➡️ Câu tiếp theo", use_container_width=True):
            if i + 1 >= len(st.session_state.questions):
                st.session_state.finished = True
            else:
                st.session_state.index += 1
                st.session_state.answered = False
                st.session_state.choice = None
            st.rerun()

else:
    score = st.session_state.score
    st.balloons()
    st.header("🏆 Hoàn thành thử thách!")

    st.metric("Điểm của bạn", f"{score}/100")

    if score == 100:
        st.success("Huyền thoại Quiz Master!")
    elif score >= 70:
        st.success("Xuất sắc! Bạn làm rất tốt!")
    elif score >= 40:
        st.info("Khá tốt! Hãy tiếp tục luyện tập.")
    else:
        st.warning("Đừng bỏ cuộc! Hãy thử lại nhé.")

    if st.button("🔄 Chơi lại", use_container_width=True):
        new_game()
        st.rerun()
