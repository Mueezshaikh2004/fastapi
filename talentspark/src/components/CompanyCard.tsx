import { useEffect, useState } from "react";
import { getCompanies } from "../Services/CompanyServices";
import type { Company } from "../types/Company";

function CompanyCard() {
  const [companies, setCompanies] = useState<Company[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchCompanies() {
      try {
        const data = await getCompanies();
        setCompanies(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unable to load companies");
      } finally {
        setLoading(false);
      }
    }

    fetchCompanies();
  }, []);

  if (loading) {
    return <div>Loading companies...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <section>
      <h2>Companies</h2>
      {companies.map((company) => (
        <div key={company.id}>
          <h3>{company.name}</h3>
          <p>{company.email}</p>
          <p>{company.phone}</p>
          <p>{company.location}</p>
        </div>
      ))}
    </section>
  );
}

export default CompanyCard;
