// Custom types

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
