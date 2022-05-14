import axios from "axios";

export interface IUser {
  id?: number;
  email: string;
  first_name: string;
  last_name: string;
  avatar: string;
}

export interface RequestInterface {
  page: number;
  per_page: number;
  total: number;
  total_pages: number;
  data: IUser[];
}

export abstract class UsersApi {
  private static usersAxios = axios.create();

  static async getAllUsers(): Promise<IUser[]> {
    const url = "https://reqres.in/api/users";
    const response = await this.usersAxios.get<RequestInterface>(url);
    return response.data.data;
  }
}
