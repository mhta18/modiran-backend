import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getBooks } from "../services/api";

function BooksSection() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        setLoading(true);
        const response = await getBooks();
        // Handle DRF list or paginated response (.results)
        const data = response.data.results || response.data;
        setBooks(data);
      } catch (err) {
        console.error("Error fetching books:", err);
        setError("خطا در دریافت اطلاعات کتاب‌ها");
      } finally {
        setLoading(false);
      }
    };

    fetchBooks();
  }, []);

  return (
    <section id="books" className="books-section" dir="rtl">
      <div className="books-container">
        <div className="books-header">
          <div>
            <span className="section-label">کتابخانه مدیران</span>
            <h2>
              کتاب‌هایی برای <span>بهتر فکر کردن</span>
            </h2>
            <p>
              مجموعه‌ای از کتاب‌های منتخب در حوزه مدیریت، رهبری، کسب‌وکار و توسعه سازمانی.
            </p>
          </div>

          <Link to="/books" className="section-more-link">
            مشاهده همه کتاب‌ها
            <span>←</span>
          </Link>
        </div>

        {loading ? (
          <div className="loading-spinner" style={{ textAlign: "center", padding: "40px" }}>
            <p>در حال بارگذاری کتاب‌ها...</p>
          </div>
        ) : error ? (
          <div className="error-message" style={{ textAlign: "center", color: "#e11d48", padding: "20px" }}>
            <p>{error}</p>
          </div>
        ) : (
          <div className="books-grid">
            {books.map((book) => {
              const imageUrl = book.image || "/images/books/default.webp";

              return (
                <article className="book-card" key={book.id}>
                  <div className="book-image-wrapper">
                    <img src={imageUrl} alt={book.title} className="book-image" />
                    <span className="book-category">{book.category}</span>
                  </div>

                  <div className="book-content">
                    <h3>{book.title}</h3>
                    <div className="book-author">نویسنده: {book.author}</div>
                    <p>{book.description}</p>

                    <Link to={`/books/${book.id}`} className="book-link">
                      مطالعه بیشتر
                      <span>←</span>
                    </Link>
                  </div>
                </article>
              );
            })}
          </div>
        )}
      </div>
    </section>
  );
}

export default BooksSection;