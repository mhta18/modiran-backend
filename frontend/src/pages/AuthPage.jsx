import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser, registerUser } from '../services/api';
import './AuthPage.css';

const AuthPage = () => {
  const [isSignUp, setIsSignUp] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // تغییر فیلد نام کاربری به ایمیل برای ورود
  const [loginData, setLoginData] = useState({ email: '', password: '' });

  const [signUpData, setSignUpData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    password: ''
  });

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      // ارسال درخواست لاگین (کوکی‌ها به صورت خودکار توسط مرورگر ذخیره می‌شوند)
      const response = await loginUser(loginData);
      console.log("Server response:", response.data);

      navigate('/dashboard'); // هدایت به داشبورد

    } catch (err) {
      console.error("Login error:", err.response?.data || err);
      const errorMsg =
        err.response?.data?.non_field_errors?.[0] ||
        err.response?.data?.detail ||
        'خطا در ورود: ایمیل یا رمز عبور اشتباه است.';
      alert(errorMsg);
    } finally {
      setLoading(false);
    }
  };

  const handleSignUpSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await registerUser(signUpData);
      alert('حساب کاربری با موفقیت ساخته شد. اکنون می‌توانید وارد شوید.');
      setIsSignUp(false); // انتقال به فرم ورود
    } catch (err) {
      console.error("Register error:", err.response?.data || err);
      alert('خطا در ثبت‌نام. ممکن است ایمیل از قبل ثبت شده باشد یا اطلاعات ناقص باشد.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper" dir="rtl">
      <div className={`auth-box ${isSignUp ? 'signup-mode' : ''}`}>

        {/* فرم ورود با ایمیل و رمز عبور */}
        <div className="form-panel signin-panel">
          <form onSubmit={handleLoginSubmit}>
            <h2>ورود به حساب کاربری</h2>
            <div className="field-group">
              <label>آدرس ایمیل</label>
              <input
                type="email"
                required
                value={loginData.email}
                onChange={(e) => setLoginData({ ...loginData, email: e.target.value })}
                placeholder="example@modiran.com"
              />
            </div>
            <div className="field-group">
              <label>رمز عبور</label>
              <input
                type="password"
                required
                value={loginData.password}
                onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
                placeholder="••••••••"
              />
            </div>
            <div className="form-meta">
              <label><input type="checkbox" /> مرا به خاطر بسپار</label>
              <a href="#forgot">فراموشی رمز عبور؟</a>
            </div>
            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? 'در حال ورود...' : 'ورود به سیستم'}
            </button>
            <p className="toggle-hint">
              حساب کاربری ندارید؟ <span onClick={() => setIsSignUp(true)} style={{ cursor: 'pointer', color: '#139a9c', fontWeight: 'bold' }}>ثبت‌نام کنید</span>
            </p>
          </form>
        </div>

        {/* فرم ثبت‌نام با نام، نام خانوادگی، ایمیل و رمز عبور */}
        <div className="form-panel signup-panel">
          <form onSubmit={handleSignUpSubmit}>
            <h2>ایجاد حساب جدید</h2>
            <div className="field-group">
              <label>نام</label>
              <input
                type="text"
                required
                value={signUpData.first_name}
                onChange={(e) => setSignUpData({ ...signUpData, first_name: e.target.value })}
                placeholder="نام خود را وارد کنید"
              />
            </div>
            <div className="field-group">
              <label>نام خانوادگی</label>
              <input
                type="text"
                required
                value={signUpData.last_name}
                onChange={(e) => setSignUpData({ ...signUpData, last_name: e.target.value })}
                placeholder="نام خانوادگی خود را وارد کنید"
              />
            </div>
            <div className="field-group">
              <label>آدرس ایمیل</label>
              <input
                type="email"
                required
                value={signUpData.email}
                onChange={(e) => setSignUpData({ ...signUpData, email: e.target.value })}
                placeholder="example@modiran.com"
              />
            </div>
            <div className="field-group">
              <label>رمز عبور</label>
              <input
                type="password"
                required
                value={signUpData.password}
                onChange={(e) => setSignUpData({ ...signUpData, password: e.target.value })}
                placeholder="حداقل ۸ کاراکتر"
              />
            </div>
            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? 'در حال ثبت نام...' : 'ایجاد حساب کاربری'}
            </button>
            <p className="toggle-hint">
              قبلاً ثبت‌نام کرده‌اید؟ <span onClick={() => setIsSignUp(false)} style={{ cursor: 'pointer', color: '#139a9c', fontWeight: 'bold' }}>وارد شوید</span>
            </p>
          </form>
        </div>

        {/* لایه مورب و متحرک (Skewed Overlay) */}
        <div className="skew-container">
          <div className="skew-blade">
            <div className="blade-content signin-info">
              <span className="brand-title">MODIRAN</span>
              <h1>خوش آمدید</h1>
              <p>جهت دسترسی به خدمات ارشد مدیریت و شبکه مشاوران وارد شوید.</p>
            </div>
            <div className="blade-content signup-info">
              <span className="brand-title">MODIRAN</span>
              <h1>آغاز مسیر رشد</h1>
              <p>با ایجاد حساب کاربری، به شبکه اختصاصی مشاوران بپیوندید.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default AuthPage;