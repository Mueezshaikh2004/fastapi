import { getCompanies } from "../Services/CompanyServices";
import { useEffect, useeffect, useState } from"react";
import {Company} from "../types/Company";

function CompanyCard() {

    const [companies, setCompany] = useState<Company[]>([]);
    async function fetchCompanies() {
        const companies = await getCompanies();
        setCompanies(companies);
    }
    useEffect(() => {
        fetchCompanies();
    },[]);
    return 

