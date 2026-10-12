import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getCourses } from "../services/api";

function CoursesSection() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        setLoading(true);
        const response = await getCourses();
        // پشتیبانی از پاسخ‌های معمولی DRF یا ساختار صفحه‌بندی شده (.results)
        const data = response.data.results || response.data;
        setCourses(data);
      } catch (err) {
        console.error("Error fetching courses:", err);
        setError("خطا در دریافت اطلاعات دوره‌ها");
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  return (
    <section id="courses" className="courses-section" dir="rtl">
      <div className="courses-container">
        <div className="courses-header">
          <div>
            <span className="section-label">آموزش و توسعه</span>
            <h2>
              مهارت‌هایی برای <span>مدیران آینده</span>
            </h2>
            <p>
              دوره‌های آموزشی تخصصی برای مدیران، کارشناسان و علاقه‌مندان به توسعه کسب‌وکار.
            </p>
          </div>

          <Link to="/events" className="section-more-link">
            مشاهده همه دوره‌ها
            <span>←</span>
          </Link>
        </div>

        {loading ? (
          <div className="loading-spinner" style={{ textAlign: "center", padding: "40px" }}>
            <p>در حال بارگذاری دوره‌ها...</p>
          </div>
        ) : error ? (
          <div className="error-message" style={{ textAlign: "center", color: "#e11d48", padding: "20px" }}>
            <p>{error}</p>
          </div>
        ) : (
          <div className="courses-grid">
            {courses.map((course) => (
              <article className="course-card" key={course.id}>
                <div className="course-top">
                  <span className="course-type">{course.type}</span>
                  <span className="course-level">{course.level}</span>
                </div>

                <div className="course-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <polygon points="12 2 2 7 12 12 22 7 12 2" />
                    <polyline points="2 17 12 22 22 17" />
                    <polyline points="2 12 12 17 22 12" />
                  </svg>
                </div>

                <h3>{course.title}</h3>
                <p className="course-instructor">مدرس: {course.instructor}</p>

                <div className="course-info">
                  <div>
                    <span>مدت دوره:</span>
                    <strong>{course.duration}</strong>
                  </div>
                  <div>
                    <span>فرمت:</span>
                    <strong>{course.type}</strong>
                  </div>
                </div>

                <Link to={`/courses/${course.id}`} className="course-button">
                  مشاهده دوره
                  <span>←</span>
                </Link>
              </article>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}

export default CoursesSection;