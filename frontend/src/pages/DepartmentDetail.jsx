import React, { useState, useEffect } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import { getDepartmentByKey } from "../services/api";

const DepartmentDetail = () => {
  const { slug } = useParams();
  const navigate = useNavigate();

  const deptKey = slug ? slug.toLowerCase() : "management";
  const [department, setDepartment] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeSectionId, setActiveSectionId] = useState("");

  useEffect(() => {
    const fetchDepartment = async () => {
      try {
        setLoading(true);
        const response = await getDepartmentByKey(deptKey);
        const deptData = response.data;
        
        // ساختاردهی پویای بخش‌ها بر اساس دوره‌های دریافت شده از دیتابیس
        // فرض بر این است که دوره‌ها دارای ویژگی course_type یا دسته‌بندی هستند
        const courses = deptData.courses || [];
        
        const podmaniCourses = courses.filter(c => c.type === "پودمانی" || !c.type);
        const singleCourses = courses.filter(c => c.type === "تک دوره‌ای" || c.type === "کارگاهی");
        const otherCourses = courses.filter(c => c.type && c.type !== "پودمانی" && c.type !== "تک دوره‌ای" && c.type !== "کارگاهی");

        const sections = [
          {
            id: "podmani",
            sidebarTitle: `آموزش‌های پودمانی ${deptData.title}`,
            heading: `آموزش‌های پودمانی ${deptData.title}`,
            cards: podmaniCourses.map(c => ({
              id: c.id,
              title: c.title,
              icon: deptData.icon || "📚",
            })),
          },
          {
            id: "single",
            sidebarTitle: `آموزش‌های تک دوره‌ای ${deptData.title}`,
            heading: `آموزش‌های تک دوره‌ای ${deptData.title}`,
            cards: singleCourses.map(c => ({
              id: c.id,
              title: c.title,
              icon: deptData.icon || "🧠",
            })),
          },
        ];

        if (otherCourses.length > 0) {
          sections.push({
            id: "other",
            sidebarTitle: `سایر دوره‌های ${deptData.title}`,
            heading: `سایر دوره‌های ${deptData.title}`,
            cards: otherCourses.map(c => ({
              id: c.id,
              title: c.title,
              icon: deptData.icon || "✨",
            })),
          });
        }

        // بخش دانلود ثابت برای هر دپارتمان
        sections.push({
          id: "download",
          sidebarTitle: "دانلود برنامه کلی دپارتمان",
          heading: "دانلود برنامه کلی دپارتمان",
          isDownload: true,
          content: {
            title: `دفترچه راهنمای جامع ${deptData.title}`,
            description: `جهت دریافت پکیج کامل سرفصل‌ها و تقویم آموزشی ${deptData.title}، فایل زیر را دریافت کنید.`,
            fileSize: "2.4 مگابایت",
          },
        });

        setDepartment({
          ...deptData,
          sections,
        });

        if (sections.length > 0) {
          setActiveSectionId(sections[0].id);
        }
      } catch (err) {
        console.error("Error fetching department detail:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchDepartment();
  }, [deptKey]);

  if (loading) {
    return (
      <div style={{ textAlign: "center", padding: "80px 20px", direction: "rtl", color: "#ffffff" }}>
        <h2>در حال بارگذاری اطلاعات دپارتمان...</h2>
      </div>
    );
  }

  if (!department) {
    return (
      <div style={{ textAlign: "center", padding: "80px 20px", direction: "rtl" }}>
        <h2>اطلاعات این دپارتمان هنوز ثبت نشده است.</h2>
        <Link to="/" style={{ color: "#139a9c", marginTop: "15px", display: "inline-block" }}>
          بازگشت به صفحه اصلی
        </Link>
      </div>
    );
  }

  const currentSection =
    department.sections.find((sec) => sec.id === activeSectionId) || department.sections[0];

  return (
    <div
      style={{
        maxWidth: "1200px",
        margin: "40px auto",
        padding: "0 20px",
        direction: "rtl",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          marginBottom: "40px",
          color: "var(--text-primary, #0b2545)",
          fontWeight: "bold",
        }}
      >
        {department.title}
      </h1>

      <div style={{ display: "flex", gap: "30px", alignItems: "flex-start", flexWrap: "wrap" }}>
        {/* سایدبار سمت راست */}
        <div
          style={{
            flex: "0 0 280px",
            backgroundColor: "rgba(255, 255, 255, 0.05)",
            border: "1px solid rgba(255, 255, 255, 0.1)",
            borderRadius: "12px",
            overflow: "hidden",
            width: "100%",
          }}
        >
          {department.sections.map((sec, index) => {
            const isActive = sec.id === currentSection.id;
            return (
              <button
                key={sec.id}
                type="button"
                onClick={() => setActiveSectionId(sec.id)}
                style={{
                  width: "100%",
                  textAlign: "right",
                  padding: "16px 18px",
                  fontSize: "13px",
                  border: "none",
                  borderBottom:
                    index !== department.sections.length - 1
                      ? "1px solid rgba(255, 255, 255, 0.1)"
                      : "none",
                  backgroundColor: isActive ? "rgba(19, 154, 156, 0.15)" : "transparent",
                  color: isActive ? "#139a9c" : "inherit",
                  fontWeight: isActive ? "bold" : "normal",
                  cursor: "pointer",
                  transition: "all 0.2s ease",
                  borderRight: isActive
                    ? "4px solid #139a9c"
                    : "4px solid transparent",
                }}
              >
                {sec.sidebarTitle}
              </button>
            );
          })}
        </div>

        {/* بخش اصلی محتوای کارت‌ها */}
        <div style={{ flex: 1, minWidth: "300px" }}>
          <h2
            style={{
              fontSize: "18px",
              marginBottom: "24px",
              color: "var(--text-primary, #ffffff)",
              fontWeight: "700",
            }}
          >
            {currentSection.heading}
          </h2>

          {!currentSection.isDownload ? (
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(170px, 1fr))",
                gap: "20px",
              }}
            >
              {currentSection.cards && currentSection.cards.length > 0 ? (
                currentSection.cards.map((card) => (
                  <div
                    key={card.id}
                    onClick={() => navigate(`/courses/${card.id}`)}
                    style={{
                      backgroundColor: "rgba(255, 255, 255, 0.03)",
                      border: "1px solid rgba(255, 255, 255, 0.1)",
                      borderRadius: "12px",
                      padding: "24px 16px",
                      textAlign: "center",
                      boxShadow: "0 4px 12px rgba(0,0,0,0.03)",
                      transition: "transform 0.2s ease, box-shadow 0.2s ease",
                      cursor: "pointer",
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.transform = "translateY(-4px)";
                      e.currentTarget.style.boxShadow =
                        "0 8px 20px rgba(0,0,0,0.15)";
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.transform = "translateY(0)";
                      e.currentTarget.style.boxShadow =
                        "0 4px 12px rgba(0,0,0,0.03)";
                    }}
                  >
                    <div style={{ fontSize: "40px", marginBottom: "12px" }}>
                      {card.icon}
                    </div>
                    <div
                      style={{
                        fontSize: "13px",
                        fontWeight: "600",
                        color: "var(--text-primary, #ffffff)",
                        lineHeight: "1.5",
                      }}
                    >
                      {card.title}
                    </div>
                  </div>
                ))
              ) : (
                <p style={{ color: "#94a3b8" }}>موردی برای نمایش وجود ندارد.</p>
              )}
            </div>
          ) : (
            <div
              style={{
                backgroundColor: "rgba(255, 255, 255, 0.03)",
                border: "1px solid rgba(255, 255, 255, 0.1)",
                borderRadius: "12px",
                padding: "24px",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                gap: "20px",
                flexWrap: "wrap",
              }}
            >
              <div>
                <h3 style={{ fontSize: "15px", fontWeight: "bold", marginBottom: "8px", color: "#fff" }}>
                  {currentSection.content?.title}
                </h3>
                <p style={{ fontSize: "13px", color: "#94a3b8", margin: 0 }}>
                  {currentSection.content?.description}
                </p>
              </div>
              <button
                style={{
                  backgroundColor: "#139a9c",
                  color: "#ffffff",
                  border: "none",
                  padding: "10px 20px",
                  borderRadius: "8px",
                  fontWeight: "bold",
                  cursor: "pointer",
                  whiteSpace: "nowrap",
                }}
              >
                📥 دریافت فایل ({currentSection.content?.fileSize})
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default DepartmentDetail;