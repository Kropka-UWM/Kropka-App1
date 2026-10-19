// Custom types

export type ErrorMessage = string | null;

type UserType = "leader" | "student" | "student_leader" | "company" | null;

export interface User {
  name: string | null;
  lastName?: string | null;
  email: string | null;
  password: string | null;
  userType: UserType;
  userName: string;
  loggedIn?: boolean;
}

export interface LoginData {
  email: string;
  password: string;
}

export interface Student {
  id: string;
  first_name: string;
  last_name: string;
  email: string;
  company: string;
}

export interface ResponseData {
  data: unknown;
}

export interface Notification {
  text: string;
  toastClass: string;
  textClass: string;
}
