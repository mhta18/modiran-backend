import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getSolutions } from "../services/api";

function SolutionsSection() {
  const [solutions, setSolutions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSolutions = async () => {
      try {
        setLoading(true);
        const response = await getSolutions();
        // Handle standard DRF list or paginated response (.results)
        const data = response.data.results || response.data;
        setSolutions(data);
      } catch (err) {
        console.error("Error fetching solutions:", err);
        setError("خطا در دریافت اطلاعات راهکارها");
      } finally {
        setLoading(false);
      }
    };

    fetchSolutions();
  }, []);

  // Helper to safely format features (whether returned as Array or String/CSV from DRF)
  const parseFeatures = (features) => {
    if (Array.isArray(features)) return features;
    if (typeof features === "string") return features.split(",").map((f) => f.trim());
    return [];
  };

  return (
    <section id="solutions" className="solutions-section" dir="rtl">
      <div className="solutions-container">
        <div className="solutions-header">
          <span className="section-label">راهکارهای تخصصی</span>
          <h2>
            راهکارهایی برای <span>رشد و توسعه سازمان</span>
          </h2>
          <p>
            با کمک شبکه‌ای از مشاوران و متخصصان باتجربه، چالش‌های سازمان خود را
            شناسایی کرده و برای آن‌ها راهکارهای عملی و تخصصی دریافت کنید.
          </p>
        </div>

        {loading ? (
          <div className="loading-spinner" style={{ textAlign: "center", padding: "40px" }}>
            <p>در حال بارگذاری راهکارها...</p>
          </div>
        ) : error ? (
          <div className="error-message" style={{ textAlign: "center", color: "#e11d48", padding: "20px" }}>
            <p>{error}</p>
          </div>
        ) : (
          <div className="solutions-grid">
            {solutions.map((solution) => {
              const featuresList = parseFeatures(solution.features);
              // Ensure image URL handles both media paths and fallbacks
              const imageUrl = solution.image || "/images/solutions/default.webp";

              return (
                <article className="solution-card" key={solution.id}>
                  <div
                    className="solution-image-wrapper"
                    style={{
                      width: "100%",
                      height: "200px",
                      overflow: "hidden",
                      borderRadius: "12px",
                      marginBottom: "10px",
                    }}
                  >
                    <img
                      src={imageUrl}
                      alt={solution.title}
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "cover",
                        display: "block",
                      }}
                    />
                  </div>

                  <h3>{solution.title}</h3>
                  <p>{solution.description}</p>

                  {featuresList.length > 0 && (
                    <div className="solution-features">
                      {featuresList.map((feature, idx) => (
                        <span key={idx}>
                          <span className="feature-check">✓</span>
                          {feature}
                        </span>
                      ))}
                    </div>
                  )}

                  <Link to={`/consultants?solution=${solution.id}`} className="solution-link">
                    مشاهده مشاوران
                    <span>←</span>
                  </Link>
                </article>
              );
            })}
          </div>
        )}
      </div>
    </section>
  );
}

export default SolutionsSection;