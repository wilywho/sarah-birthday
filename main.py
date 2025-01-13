import streamlit as st
import random
import time

# Daftar hadiah buku
books = [
    "The Devotion of Suspect X by Keigo Higashino",
    "Murder on the Orient Express by Agatha Christie",
    "The Hound of the Baskervilles by Sir Arthur Conan Doyle",
    "Confession by Kanae Minato",
    "The Murder of Roger Ackroyd by Agatha Christie",
    "The Poisoned Chocolate Cases by Anthony Berkley",
    "The Great Gatsby by F. Scott Fitzgerald"
]

# Buku dengan prioritas 100% pada generate pertama dan kedua
first_book = "The Hound of the Baskervilles by Sir Arthur Conan Doyle"
second_book = "Murder on the Orient Express by Agatha Christie"

# Simpan state untuk kontrol pemberian hadiah
if "is_first_generate" not in st.session_state:
    st.session_state.is_first_generate = True
if "is_second_generate" not in st.session_state:
    st.session_state.is_second_generate = True

# Simpan state hadiah buku yang telah dibuka
if "book_1_opened" not in st.session_state:
    st.session_state.book_1_opened = False
if "book_2_opened" not in st.session_state:
    st.session_state.book_2_opened = False

# Judul halaman
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="animation: fadeIn 2s;">🎉 Happy Birthday! 🎂</h1>
    </div>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Input nama penerima ucapan
name = "Sarah"  # Menetapkan nama secara langsung

if name:
    st.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
        <h2>🎊 Selamat ulang tahun, Sarah! 🎉</h2>
        <p style="margin-top: 20px;">Barakallah fii umrik, semoga semua impian dan target di tahun 2025 tercapai yaa! Sukses selalu! 🎁</p>
    </div>
    """,
    unsafe_allow_html=True
    )


    # Tentukan hadiah berdasarkan urutan generate
    if st.session_state.is_first_generate:
        book_1 = first_book
        st.session_state.is_first_generate = False
    elif st.session_state.is_second_generate:
        book_1 = second_book
        st.session_state.is_second_generate = False
    else:
        # Pilih buku acak untuk berikutnya
        book_1 = random.choice(books)

    # Pilih buku kedua secara acak dari daftar
    book_2 = random.choice([b for b in books if b != book_1])

    st.subheader("🎁 Hadiah untuk Kamu:")

    # Tombol untuk menampilkan hadiah pertama
    if st.button("Open Hadiah 1") and not st.session_state.book_1_opened:
        with st.spinner("Membuka hadiah pertama..."):
            time.sleep(2)  # Tunggu 2 detik
        st.session_state.book_1_opened = True  # Tandai hadiah pertama sudah dibuka
        st.markdown(
            f"""
            <div style="animation: fadeIn 2s; text-align: center;">
                📚 <strong>{book_1}</strong>
            </div>
            <style>
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # Tombol untuk menampilkan hadiah kedua
    if st.button("Open Hadiah 2") and not st.session_state.book_2_opened:
        with st.spinner("Membuka hadiah kedua..."):
            time.sleep(2)  # Tunggu 2 detik
        st.session_state.book_2_opened = True  # Tandai hadiah kedua sudah dibuka
        st.markdown(
            f"""
            <div style="animation: fadeIn 2s; text-align: center;">
                📚 <strong>{book_2}</strong>
            </div>
            <style>
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
            </style>
            """,
            unsafe_allow_html=True
        )


st.write("Hadiah akan diantar ke tempat tujuan dalam rentang waktu 1-3 hari kerja")
# Footer
st.write("---")
st.write("✨ Dibuat dengan Streamlit untuk merayakan momen spesial! 🎈")
st.write("Note: Hadiah akan dipilih otomatis secara random pada pukul 23.00 WIB apabila tidak dibuka manual")


