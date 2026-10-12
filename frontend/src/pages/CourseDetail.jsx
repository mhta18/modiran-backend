import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { getCourseById } from '../services/api';

const CourseDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [activeTab, setActiveTab] = useState('info');
  const [openFaq, setOpenFaq] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedGroup, setSelectedGroup] = useState(null);

  useEffect(() => {
    const fetchCourseDetail = async () => {
      try {
        setLoading(true);
        const response = await getCourseById(id);
        setCourse(response.data);
      } catch (err) {
        console.error("Error fetching course details:", err);
        setError("دوره مورد نظر یافت نشد.");
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      fetchCourseDetail();
    }
  }, [id]);

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '100px 20px', direction: 'rtl', color: '#0f172a' }}>
        <h2>در حال بارگذاری اطلاعات دوره...</h2>
      </div>
    );
  }

  if (error || !course) {
    return (
      <div style={{ textAlign: 'center', padding: '100px 20px', direction: 'rtl' }}>
        <h2>{error || "دوره مورد نظر یافت نشد."}</h2>
        <Link to="/" style={{ color: '#139a9c', marginTop: '15px', display: 'inline-block' }}>
          بازگشت به صفحه اصلی
        </Link>
      </div>
    );
  }

  const tabs = [
    { id: 'info', label: 'اطلاعات برگزاری دوره', icon: 'ℹ️' },
    { id: 'intro', label: 'معرفی دوره', icon: '📖' },
    { id: 'syllabus', label: 'سرفصل‌ها', icon: '📋' },
    { id: 'audience', label: 'مخاطبان و مهارت‌ها', icon: '👥' },
    { id: 'teacher', label: 'مدرس', icon: '👨‍🏫' },
    { id: 'certificates', label: 'مدارک و گواهی‌نامه‌ها', icon: '🏅' },
    { id: 'faq', label: 'سوالات پرتکرار', icon: '❓' },
  ];

  const handleContactExpert = () => {
    window.location.href = `tel:02188888888`;
  };

  const handleOpenRegister = (groupName = null) => {
    setSelectedGroup(groupName);
    setIsModalOpen(true);
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '30px auto', padding: '0 20px', direction: 'rtl' }}>

      {/* نوار مسیر (Breadcrumb) */}
      <div style={{ fontSize: '13px', color: '#64748b', marginBottom: '20px' }}>
        <Link to="/" style={{ color: '#64748b', textDecoration: 'none' }}>خانه</Link> {' > '}
        <span style={{ color: '#139a9c', fontWeight: 'bold' }}>{course.title}</span>
      </div>

      {/* هدر دوره */}
      <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '16px', padding: '30px', marginBottom: '30px', boxShadow: '0 4px 15px rgba(0,0,0,0.05)' }}>
        <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '10px', color: '#0f172a' }}>{course.title}</h1>
        <p style={{ color: '#139a9c', fontSize: '14px', marginBottom: '15px', fontWeight: 'bold' }}>
          {course.type ? `نوع دوره: ${course.type}` : 'دوره تخصصی'} | مدرس: {course.instructor || 'اساتید مجرب'} | مدت: {course.duration || 'نامشخص'}
        </p>
        <p style={{ color: '#334155', fontSize: '15px', lineHeight: '1.8', maxWidth: '900px' }}>
          {course.description || "توضیحات تکمیلی برای این دوره ثبت نشده است."}
        </p>

        <div style={{ display: 'flex', gap: '15px', marginTop: '25px', flexWrap: 'wrap' }}>
          <button
            onClick={() => handleOpenRegister()}
            style={{ backgroundColor: '#139a9c', color: '#fff', border: 'none', padding: '12px 28px', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer', fontSize: '14px' }}>
            پیش ثبت‌نام دوره ←
          </button>
          <button
            onClick={handleContactExpert}
            style={{ backgroundColor: '#fff', color: '#139a9c', border: '2px solid #139a9c', padding: '12px 24px', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer', fontSize: '14px' }}>
            تماس با کارشناس دوره 📞
          </button>
        </div>
      </div>

      {/* تب‌های بالای صفحه */}
      <div style={{ display: 'flex', gap: '10px', overflowX: 'auto', paddingBottom: '10px', marginBottom: '30px', borderBottom: '2px solid #e2e8f0' }}>
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              padding: '12px 20px',
              borderRadius: '30px',
              border: 'none',
              backgroundColor: activeTab === tab.id ? '#139a9c' : '#f1f5f9',
              color: activeTab === tab.id ? '#ffffff' : '#475569',
              fontWeight: activeTab === tab.id ? 'bold' : '500',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
              fontSize: '13px',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              transition: 'all 0.2s ease'
            }}
          >
            <span>{tab.icon}</span>
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* محتوای تب‌ها */}
      <div>
        {activeTab === 'info' && (
          <div>
            <h2 style={{ fontSize: '18px', marginBottom: '20px', color: '#0f172a' }}>اطلاعات کلی دوره</h2>
            <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
              <div><strong>عنوان دوره:</strong> {course.title}</div>
              <div><strong>مدرس:</strong> {course.instructor || "تعیین نشده"}</div>
              <div><strong>مدت زمان:</strong> {course.duration || "تعیین نشده"}</div>
              <div><strong>سطح دوره:</strong> {course.level || "عمومی"}</div>
              <div><strong>نوع دوره:</strong> {course.type || "تخصصی"}</div>
            </div>
          </div>
        )}

        {activeTab === 'intro' && (
          <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '25px', lineHeight: '2', color: '#334155' }}>
            <h3 style={{ color: '#0f172a', marginBottom: '15px' }}>معرفی جامع دوره</h3>
            <p>{course.description}</p>
          </div>
        )}

        {activeTab === 'syllabus' && (
          <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '25px' }}>
            <h3 style={{ color: '#0f172a', marginBottom: '15px' }}>سرفصل‌های آموزشی</h3>
            <p style={{ color: '#475569' }}>سرفصل‌های تخصصی این دوره متناسب با استانداردهای بازار کار تنظیم شده است.</p>
          </div>
        )}

        {activeTab === 'audience' && (
          <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '25px' }}>
            <h3 style={{ color: '#0f172a', marginBottom: '15px' }}>مخاطبان دوره</h3>
            <p style={{ color: '#475569' }}>این دوره برای تمامی علاقه‌مندان، متخصصان و فعالان این حوزه طراحی شده است.</p>
          </div>
        )}

        {activeTab === 'teacher' && (
          <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '25px' }}>
            <h3 style={{ color: '#0f172a', marginBottom: '10px' }}>مدرس دوره: {course.instructor || "استاد برتر مجموعه"}</h3>
            <p style={{ color: '#334155', fontSize: '14px', lineHeight: '1.8' }}>دارای سابقه درخشان در تدریس و اجرای پروژه‌های حرفه‌ای.</p>
          </div>
        )}

        {activeTab === 'certificates' && (
          <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '25px' }}>
            <h3 style={{ color: '#0f172a', marginBottom: '15px' }}>مدارک و گواهینامه‌های دوره</h3>
            <p style={{ color: '#334155', fontSize: '14px', lineHeight: '1.8' }}>
              پس از اتمام موفقیت‌آمیز دوره، مدرک معتبر و قابل ترجمه اعطا خواهد شد.
            </p>
          </div>
        )}

        {activeTab === 'faq' && (
          <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '12px', padding: '25px' }}>
            <h3 style={{ color: '#0f172a', marginBottom: '15px' }}>سوالات پرتکرار</h3>
            <p style={{ color: '#475569' }}>پاسخ به سوالات متداول درباره نحوه ثبت‌نام و برگزاری دوره‌ها.</p>
          </div>
        )}
      </div>

      {/* مدال ثبت‌نام */}
      {isModalOpen && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000 }}>
          <div style={{ backgroundColor: '#fff', borderRadius: '16px', padding: '30px', width: '90%', maxWidth: '450px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ marginBottom: '15px', color: '#0f172a' }}>فرم پیش ثبت‌نام دوره</h3>
            <p style={{ color: '#139a9c', fontSize: '13px', marginBottom: '15px' }}>دوره: {course.title}</p>
            <form onSubmit={(e) => { e.preventDefault(); alert('درخواست ثبت‌نام شما با موفقیت ثبت شد.'); setIsModalOpen(false); }}>
              <input type="text" placeholder="نام و نام خانوادگی" required style={{ width: '100%', padding: '10px', marginBottom: '12px', borderRadius: '8px', border: '1px solid #cbd5e1', boxSizing: 'border-box' }} />
              <input type="tel" placeholder="شماره موبایل" required style={{ width: '100%', padding: '10px', marginBottom: '20px', borderRadius: '8px', border: '1px solid #cbd5e1', boxSizing: 'border-box' }} />
              <div style={{ display: 'flex', gap: '10px' }}>
                <button type="submit" style={{ flex: 1, backgroundColor: '#139a9c', color: '#fff', border: 'none', padding: '10px', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer' }}>تایید و ارسال</button>
                <button type="button" onClick={() => setIsModalOpen(false)} style={{ flex: 1, backgroundColor: '#f1f5f9', color: '#475569', border: 'none', padding: '10px', borderRadius: '8px', fontWeight: 'bold', cursor: 'pointer' }}>انصراف</button>
              </div>
            </form>
          </div>
        </div>
      )}

    </div>
  );
};

export default CourseDetail;