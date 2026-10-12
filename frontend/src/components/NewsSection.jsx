import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getNews } from "../services/api";

function NewsSection() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        setLoading(true);
        const response = await getNews();
        // پشتیبانی از ساختار لیست معمولی یا صفحه‌بندی شده DRF (.results)
        const data = response.data.results || response.data;
        setNews(data);
      } catch (err) {
        console.error("Error fetching news:", err);
        setError("خطا در دریافت اطلاعات اخبار و مقالات");
      } finally {
        setLoading(false);
      }
    };

    fetchNews();
  }, []);

  return (
    <section id="news" className="news-section" dir="rtl">
      <div className="news-container">
        <div className="news-header">
          <div>
            <span className="section-label">دانش و بینش</span>
            <h2>
              آخرین مطالب <span>مدیران</span>
            </h2>
            <p>
              مقالات، تحلیل‌ها و مطالب تخصصی در حوزه مدیریت و توسعه کسب‌وکار.
            </p>
          </div>

          <Link to="/news" className="section-more-link">
            مشاهده همه مطالب
            <span>←</span>
          </Link>
        </div>

        {loading ? (
          <div className="loading-spinner" style={{ textAlign: "center", padding: "40px" }}>
            <p>در حال بارگذاری مطالب...</p>
          </div>
        ) : error ? (
          <div className="error-message" style={{ textAlign: "center", color: "#e11d48", padding: "20px" }}>
            <p>{error}</p>
          </div>
        ) : (
          <div className="news-grid">
            {news.map((item) => {
              const imageUrl = item.image || "/images/news/default.webp";

              return (
                <article className="news-card" key={item.id}>
                  <div className="news-image-wrapper">
                    <img
                      src={imageUrl}
                      alt={item.title}
                      className="news-image"
                    />
                    <span className="news-category">{item.category}</span>
                  </div>

                  <div className="news-content">
                    <div className="news-meta">
                      <span className="news-date">{item.date}</span>
                    </div>

                    <h3>{item.title}</h3>

                    <p>{item.excerpt}</p>

                    <Link to={`/news/${item.id}`} className="news-link">
                      ادامه مطلب
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

export default NewsSection;