// Custom types

import { string } from "yup";

export type ErrorMessage = string | null;

type UserType = "Admin" | "Student" | "Student leader" | "Company" | null;

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
  name: string;
  surname: string;
  email: string;
  company: string;
}

export interface ResponseData {
  data: any;
}

export interface Notification {
  text: string;
  toastClass: string;
  textClass: string;
}
