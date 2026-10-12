import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // دریافت اطلاعات کاربر لاگین‌شده از سمت سرور
  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await api.get('auth/me/');
        setUser(response.data);
      } catch (err) {
        console.error("Failed to fetch user data:", err);
        navigate('/auth');
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, [navigate]);

  const handleLogout = async () => {
    try {
      await api.post('auth/logout/');
      navigate('/auth');
    } catch (err) {
      console.error("Logout error:", err);
      navigate('/auth');
    }
  };

  if (loading) {
    return <div style={{ textAlign: 'center', marginTop: '100px', fontSize: '18px' }}>در حال بارگذاری اطلاعات...</div>;
  }

  const displayName = user ? `${user.first_name || ''} ${user.last_name || ''}`.trim() || user.email : 'کاربر محترم';

  return (
    <div style={{ backgroundColor: '#f8fafc', color: '#1e293b', minHeight: '90vh', padding: '40px 20px', direction: 'rtl', fontFamily: 'Vazirmatn, sans-serif' }}>
      <div style={{ maxWidth: '1000px', margin: '0 auto' }}>

        {/* هدر پنل */}
        <div style={{ backgroundColor: '#ffffff', padding: '24px', borderRadius: '12px', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)', border: '1px solid #e2e8f0', marginBottom: '32px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h1 style={{ color: '#0f172a', fontSize: '22px', margin: 0 }}>خوش آمدید، {displayName}</h1>
            <p style={{ color: '#64748b', fontSize: '13px', margin: '4px 0 0 0' }}>مدیریت جلسات مشاوره و فاکتورها</p>
          </div>
          <button onClick={handleLogout} style={{ backgroundColor: 'transparent', border: '1px solid #ef4444', color: '#ef4444', padding: '8px 16px', borderRadius: '6px', cursor: 'pointer', transition: 'all 0.2s' }}>
            خروج
          </button>
        </div>

        {/* بخش خالی برای داده‌های آینده */}
        <div style={{ backgroundColor: '#ffffff', padding: '40px', borderRadius: '12px', textAlign: 'center', border: '1px solid #e2e8f0', color: '#64748b' }}>
          <p style={{ fontSize: '15px', margin: 0 }}>هیچ اطلاعات یا فاکتوری برای نمایش وجود ندارد.</p>
        </div>

      </div>
    </div>
  );
};

export default Dashboard;