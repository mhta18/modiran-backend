import React, { useState, useEffect } from "react";
import { getFeedbacks } from "../services/api";

function FeedbackSection() {
    const [feedbacks, setFeedbacks] = useState([]);
    const [activeIndex, setActiveIndex] = useState(0);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchFeedbacks = async () => {
            try {
                setLoading(true);
                const response = await getFeedbacks();
                // پشتیبانی از لیست معمولی یا پاسخ صفحه‌بندی شده DRF (.results)
                const data = response.data.results || response.data;
                setFeedbacks(data);
            } catch (err) {
                console.error("Error fetching feedbacks:", err);
                setError("خطا در دریافت تجربیات مشتریان");
            } finally {
                setLoading(false);
            }
        };

        fetchFeedbacks();
    }, []);

    const nextFeedback = () => {
        if (feedbacks.length === 0) return;
        setActiveIndex((prev) => (prev + 1) % feedbacks.length);
    };

    const previousFeedback = () => {
        if (feedbacks.length === 0) return;
        setActiveIndex((prev) => (prev - 1 + feedbacks.length) % feedbacks.length);
    };

    if (loading) {
        return (
            <section id="feedback" className="feedback-section" dir="rtl">
                <div className="feedback-container" style={{ textAlign: "center", padding: "40px" }}>
                    <p>در حال بارگذاری تجربیات مشتریان...</p>
                </div>
            </section>
        );
    }

    if (error || feedbacks.length === 0) {
        return null; // یا نمایش پیام خطا بر اساس نیاز
    }

    const activeFeedback = feedbacks[activeIndex] || feedbacks[0];

    return (
        <section id="feedback" className="feedback-section" dir="rtl">
            <div className="feedback-container">
                <div className="feedback-header">
                    <span className="section-label">تجربه مشتریان</span>
                    <h2>
                        تجربه کسانی که با
                        <span> مدیران</span> همراه شده‌اند
                    </h2>
                    <p>
                        بخشی از تجربه مدیران و سازمان‌هایی که برای حل مسائل خود از خدمات مشاوره‌ای استفاده کرده‌اند.
                    </p>
                </div>

                <div className="feedback-card">
                    <div className="quote-icon">“</div>

                    <div className="feedback-content">
                        <p className="feedback-text">{activeFeedback.text}</p>

                        <div className="feedback-person">
                            <div className="person-avatar">
                                {activeFeedback.name ? activeFeedback.name.charAt(0) : "م"}
                            </div>

                            <div>
                                <h3>{activeFeedback.name}</h3>
                                <span>{activeFeedback.role}</span>
                            </div>
                        </div>
                    </div>

                    <div className="feedback-controls">
                        <button
                            type="button"
                            onClick={previousFeedback}
                            aria-label="نظر قبلی"
                        >
                            →
                        </button>

                        <span>
                            {activeIndex + 1} / {feedbacks.length}
                        </span>

                        <button
                            type="button"
                            onClick={nextFeedback}
                            aria-label="نظر بعدی"
                        >
                            ←
                        </button>
                    </div>
                </div>

                <div className="feedback-dots">
                    {feedbacks.map((feedback, index) => (
                        <button
                            key={feedback.id || index}
                            type="button"
                            className={index === activeIndex ? "active" : ""}
                            onClick={() => setActiveIndex(index)}
                            aria-label={`نظر ${index + 1}`}
                        />
                    ))}
                </div>
            </div>
        </section>
    );
}

export default FeedbackSection;