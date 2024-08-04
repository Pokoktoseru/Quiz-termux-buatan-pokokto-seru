import random

# Daftar pertanyaan dan jawaban
quiz_data = {
    "Apa ibukota Indonesia?": "Jakarta",
    "Siapakah presiden pertama Indonesia?": "Soekarno",
    "Berapa jumlah provinsi di Indonesia?": "34",
    "Apa huruf pertama dalam alfabet?": "A",
    # Tambahkan lebih banyak pertanyaan dan jawaban di sini
}

def main():
    # Tentukan jumlah pertanyaan yang akan diambil, tidak melebihi jumlah item di quiz_data
    num_questions = min(50, len(quiz_data))
    quiz_questions = random.sample(list(quiz_data.keys()), num_questions)

    # Skor awal
    score = 0

    # Mulai kuis
    print("Selamat datang di Kuis! Jawab pertanyaan berikut ini:")
    for i, question in enumerate(quiz_questions, start=1):
        print(f"\nPertanyaan {i}: {question}")
        user_answer = input("Jawaban Anda: ").strip().capitalize()

        # Periksa jawaban
        correct_answer = quiz_data[question].capitalize()
        if user_answer == correct_answer:
            print("Jawaban Anda benar!")
            score += 1
        else:
            print(f"Jawaban Anda salah. Jawaban yang benar adalah: {correct_answer}")

    # Tampilkan skor akhir
    print(f"\nKuis selesai! Skor Anda adalah {score} dari {num_questions}.")

if __name__ == "__main__":
    main()
