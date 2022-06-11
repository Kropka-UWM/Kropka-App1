import axios from "axios";

import { key } from "@/store";
import { useStore } from "vuex";

const store = useStore(key);

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

  static async getAllUsers(token: string): Promise<IUser[]> {


    const url = "http://vps-9ee2e9ea.vps.ovh.net:8000/list_students/";
    const response = await this.usersAxios.get<RequestInterface>(url, {
      headers: {
        Authorization: `JWT ${token}`,
      },
    });
    return response.data.data;
  }
}
