// Custom types

import { string } from "yup";

export type ErrorMessage = string | null;

type UserType = "Admin" | "User" | "Company" | null;

export interface User {
  name: string | null;
  email: string | null;
  password: string | null;
  userType: UserType;
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
  active: boolean;
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
