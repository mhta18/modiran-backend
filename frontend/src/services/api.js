import axios from "axios";

// تشخیص خودکار آدرس پایه بر اساس محیط اجرا
const getBaseUrl = () => {
  // اگر از Create React App استفاده می‌کنید:
  if (typeof process !== 'undefined' && process.env && process.env.REACT_APP_API_URL) {
    return process.env.REACT_APP_API_URL;
  }
  // اگر از Vite استفاده می‌کنید:
  if (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL;
  }

  // حالت پیش‌فرض بر اساس دامنه فعلی مرورگر (برای پروداکشن روی سرور)
  if (window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1") {
    return `${window.location.protocol}//${window.location.host}/api/`;
  }

  // حالت پیش‌فرض برای توسعه روی سیستم لوکال
  return "http://localhost:8000/api/";
};

const api = axios.create({
  baseURL: getBaseUrl(),
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

// Consultants
export const getConsultants = (params = {}) =>
  api.get("consultants/", { params });

export const getConsultantsBasedOnServices = (serviceIds) => {
  const query = serviceIds
    .map((id) => `service=${encodeURIComponent(id)}`)
    .join("&");

  return api.get(`consultants/?${query}`);
};

export const getConsultant = (id) =>
  api.get(`consultants/${id}/`);

// get consultant services
export const getConsultantServices = (consultantId) =>
  api.get(`consultants/${consultantId}/services/`);

// Services
export const getServices = () =>
  api.get("services/");

export const getService = (id) =>
  api.get(`services/${id}/`);

// Consultation Requests
export const getConsultationChoices = () =>
  api.get("consultation-requests/choices/");

// Events
export const getEvents = () =>
  api.get("events/");

export const getEvent = (id) =>
  api.get(`events/${id}/`);

// Event Registration
export const registerForEvent = (data) => {
  return api.post("event-registrations/", data);
};

// Consultation Requests
export const createConsultationRequest = (data) =>
  api.post("consultation-requests/", data);

// Auth
export const loginUser =  (credentials) => {
  return  api.post("auth/login/", credentials);
};

export const registerUser =  (userData) => {
  return  api.post("auth/register/", userData);
};

//Solutions
export const getSolutions = (params = {}) =>
  api.get("content/solutions/", { params });

export const getSolution = (id) =>
  api.get(`content/solutions/${id}/`);


//Books
export const getBooks = (params = {}) =>
  api.get("content/books/", { params });

export const getBook = (id) =>
  api.get(`/content/books/${id}/`);

//Course
export const getCourses = (params = {}) =>
  api.get("courses/", { params });

export const getCourseById = (id) =>
  api.get(`courses/${id}/`);

//News
export const getNews = (params = {}) =>
  api.get("content/news/", { params });

export const getNewsItem = (id) =>
  api.get(`content/news/${id}/`);

// Departments
export const getDepartments = (params = {}) =>
  api.get("departments/", { params });

export const getDepartmentByKey = (key) =>
  api.get(`departments/${key}/`);

// Feedbacks / Testimonials
export const getFeedbacks = (params = {}) =>
  api.get("content/feedbacks/", { params });

export default api;