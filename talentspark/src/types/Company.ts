export interface Job {
  id: number;
  title: string;
  salary: number;
  description?: string;
  company_id: number;
}

export interface Company {
  id: number;
  name: string;
  email: string;
  phone: string;
  location: string;
  jobs: Job[];
}