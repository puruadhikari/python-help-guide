class Solution:

    def _get_domain_list(self, domain):
        result = []
        if len(domain) == 0:
            return []

        domain_list = domain.split(".")

        for index in range(len(domain_list)):
            sub_domain = ".".join(domain_list[index:])
            result.append(sub_domain)

        return result

    def subdomain_visits(self, cpdomains):
        result_dict = {}
        output = []

        for items in cpdomains:
            item_split = items.split(" ")
            domain_count = item_split[0]
            domain_name = item_split[1]
            domain_name_list = self._get_domain_list(domain_name)

            for dn in domain_name_list:
                if dn not in result_dict:
                    result_dict[dn] = int(domain_count)
                else:
                    result_dict[dn] = result_dict[dn] + int(domain_count)

        for key, value in result_dict.items():
            output.append(str(value) + " " + key)

        return output


sol = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

print(sol.subdomain_visits(cpdomains))