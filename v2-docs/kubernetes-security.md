# Kubernetes Security

!!! info "Architectural Context"
    Detailed reference for Kubernetes Security in the context of Hardened Infrastructure.

## Standard Reference

  - [jetstack.io: Securing Istio workloads with mTLS using cert-manager](https://www.cyberark.com/venafi-and-cyberark-machine-identity-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: External Secret Operator on AKS (with Terraform) for Azure Key' Vault Integration (with Workload Identity)](https://faun.pub/external-secret-operator-on-aks-with-terraform-for-azure-key-vault-integration-with-workload-1d0c31082373)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Single Sign-On in Kubernetes](https://medium.com/@andriisumko/single-sign-on-in-kubernetes-1ad9528350ed)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone - OAuth 2.0](https://dzone.com/articles/oauth-20-beginners-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to Harden Your Kubernetes Cluster for Production 🌟](https://medium.com/better-programming/how-to-harden-your-kubernetes-cluster-for-production-7e47990efc2a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cncf.io: Kubernetes Security 🌟](https://www.cncf.io/blog/2021/03/22/kubernetes-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [redkubes.com: 10 Kubernetes Security Risks & Best Practices](https://redkubes.com/10-kubernetes-security-risks-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kasten.io: Kubernetes Ransomware Protection with Kasten K10 v4.0](https://blog.kasten.io/ransomware-protection-kasten-k10-v4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Enforce Audit Policy in Kubernetes (k8s)](https://levelup.gitconnected.com/enforce-audit-policy-in-kubernetes-k8s-34e504733300)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [magalix.com: Top 8 Kubernetes Security Best Practices 🌟](https://www.magalix.com/blog/top-8-kubernetes-security-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cncf.io: How to secure your Kubernetes control plane and node components](https://www.cncf.io/blog/2021/08/20/how-to-secure-your-kubernetes-control-plane-and-node-components)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [akhilsharma.work: The 4C's of Kubernetes Security](https://akhilsharma.work/the-4cs-of-kubernetes-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Securing the Kubernetes cluster | Lessandro Z. Ugulino](https://medium.com/@lessandro.ugulino/securing-the-kubernetes-cluster-c5ab43fe0dd0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [amazicworld.com: Top 5 security threats unique to a Kubernetes and Cloud' Native stack](https://amazicworld.com/top-5-security-threats-unique-to-a-kubernetes-and-cloud-native-stack)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [venturebeat.com: Kubernetes security will have a breakout year in 2022](https://venturebeat.com/2021/12/27/kubernetes-security-will-have-a-breakout-year-in-2022)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Comparing Kubernetes Security Frameworks and Guidance 🌟](https://medium.com/@jonathan_37674/comparing-kubernetes-security-frameworks-and-guidance-f1c2821ea733)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: How is security managed in Kubernetes clusters?](https://blog.devgenius.io/how-is-security-managed-in-kubernetes-clusters-addefffd2b0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jonathan_37674: Kubernetes Security Best Practices: Definitive' Guide](https://medium.com/@jonathan_37674/kubernetes-security-best-practices-definitive-guide-bcb546e9f529)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: From dev to admin: an easy Kubernetes privilege escalation you' should be aware of — the attack](https://faun.pub/from-dev-to-admin-an-easy-kubernetes-privilege-escalation-you-should-be-aware-of-the-attack-950e6cf76cac)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@dotdc: Is your Kubernetes API Server exposed? Learn how to' check and fix! 🌟](https://medium.com/@dotdc/is-your-kubernetes-api-server-exposed-learn-how-to-check-and-fix-609ab9638fae)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: The Core of Kubernetes Security: Clusters](https://levelup.gitconnected.com/the-core-of-kubernetes-security-clusters-5d9a69f1dba4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@codingkarma: Kubernetes Goat Part-1](https://medium.com/@codingkarma/kubernetes-goat-part-1-8718b1345a42)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@badawekoo: Limit number of processes running in a Kubernetes' pod](https://medium.com/@badawekoo/limit-number-of-processes-running-in-a-kubernetes-pod-50ccf156ec18)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/cloudyrion: Kubernetes end-to-end chain exploit](https://medium.com/cloudyrion/kubernetes-end-to-end-chain-exploit-c2be32688fd0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [xgrid.medium.com: Securing a Kubernetes cluster using TLS certificates' 🌟](https://xgrid.medium.com/securing-a-kubernetes-cluster-using-tls-certificates-5e64a6bb26de)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ahmedy.hashnode.dev: Creating TLS Certificates for K8s components with OpenSSL](https://ahmedy.hashnode.dev/creating-tls-certificates-for-k8s-components-with-openssl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [erkanzileli.medium.com: How TLS Certificates Work](https://erkanzileli.medium.com/how-tls-certificates-work-422d95f1df5e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@martin.hodges: Using a wildcard certificate within your Kubernetes' cluster](https://medium.com/@martin.hodges/using-a-wildcard-certificate-within-your-kubernetes-cluster-87c014e8dafe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudsecque.com: How to Improve the Security of Your Applications' with Kubernetes Security Scanners](https://blog.cloudsecque.com/how-to-improve-the-security-of-your-applications-with-kubernetes-security-scanners-cda97fd2f574)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [techmanyu.com: Kubernetes Security with Kube-bench and Kube-hunter 🌟](https://www.techmanyu.com/kubernetes-security-with-kube-bench-and-kube-hunter-6765bf44ebc6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aninditabasak.medium.com: A Lap around Kubernetes Security & Vulnerability' scanning Tools — checkov, kube-hunter, kube-bench & Starboard](https://aninditabasak.medium.com/a-lap-around-kubernetes-security-vulnerability-scanning-tools-checkov-kube-hunter-kube-bench-4ffda92c4cf1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [towardsdev.com: 12 Scanners to Find Security Vulnerabilities and Misconfigurations' in Kubernetes](https://towardsdev.com/12-scanners-to-find-security-vulnerabilities-and-misconfigurations-in-kubernetes-332a738d076d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Gatekeeper | K8 hardening backlog](https://faun.pub/gatekeeper-k8-hardening-backlog-956d1b6860b6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [systemweakness.com: OWASP-K8S Security: Insecure Workload Configurations](https://systemweakness.com/owasp-k8s-security-insecure-workload-configurations-c14c4028beb1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [darkreading.com: Top 10 Kubernetes Security Risks Every DevSecOps Pro Should' Know](https://www.darkreading.com/dr-tech/top-10-kubernetes-security-risks-every-devsecops-needs-to-know)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes Hardening Guidance 🌟🌟](https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aymen-abdelwahed.medium.com: K8s Operators — CIS Kubernetes Benchmarks](https://aymen-abdelwahed.medium.com/k8s-operators-cis-benchmarks-8d7915d5cb2d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Working with Service Account In Kubernetes 🌟](https://medium.com/the-programmer/working-with-service-account-in-kubernetes-df129cb4d1cc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sandeepbaldawa.medium.com: Service Accounts in K8s (Kubernetes)](https://sandeepbaldawa.medium.com/service-accounts-in-k8s-kubernetes-2779ee4fb331)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/pareture: Kubernetes Bound Projected Service Account Token Volumes' Might Surprise You](https://medium.com/pareture/kubernetes-bound-projected-service-account-token-volumes-might-surprise-you-434ff2cd1483)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: K8s — ServiceAccount Token](https://medium.com/geekculture/k8s-serviceaccount-token-313d62aee119)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [motilayo.hashnode.dev: Exploring Kubernetes Service Account Tokens and Secure' Workload Identity Federation](https://motilayo.hashnode.dev/exploring-kubernetes-service-account-tokens-and-secure-workload-identity-federation)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [overcast.blog: Kubernetes Service Accounts: A Practical Guide](https://overcast.blog/kubernetes-service-accounts-a-practical-guide-f99c1ed65483)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cncf.io: Revealing the secrets of Kubernetes secrets 🌟](https://www.cncf.io/blog/2021/04/22/revealing-the-secrets-of-kubernetes-secrets)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.doit-intl.com: Kubernetes and Secrets Management in the Cloud](https://blog.doit-intl.com/kubernetes-and-secrets-management-in-cloud-858533c20dca)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Kubernetes Secrets Explained](https://medium.com/codex/kubernetes-secrets-explained-f45baf8cefa7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Managing your sensitive information during GitOps process with Secret' Sealed](https://medium.com/@jerome_tarte/managing-your-sensitive-information-during-gitops-process-with-secret-sealed-27498c77e2b8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [enlear.academy: Sealed Secrets with Kubernetes](https://enlear.academy/sealed-secrets-with-kubernetes-a3f4d13dbc17)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/codex: Sealed Secrets for Kubernetes](https://medium.com/codex/sealed-secrets-for-kubernetes-722d643eb658)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [carlosalca.medium.com: How to manage all my K8s secrets in git securely' with Bitnami Sealed Secrets](https://carlosalca.medium.com/how-to-manage-all-my-k8s-secrets-in-git-securely-with-bitnami-sealed-secrets-43580b8fa0c7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pjame-fb.medium.com: Kubernetes Secrets from Secrets Manager using External' Secrets Operators](https://pjame-fb.medium.com/kubernetes-secrets-from-secrets-manager-using-external-secrets-operators-4819562c3b02)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mixi-developers.mixi.co.jp: Comparing External Secrets Operator with Secret' Storage CSI as Kubernetes External Secrets is Deprecated](https://mixi-developers.mixi.co.jp/compare-eso-with-secret-csi-402bf37f20bc?gi=a7ce4398a8d7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Secrets | Kubernetes](https://faun.pub/secrets-kubernetes-298ea8dd9911)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@knoldus: Using sealed secrets in Kubernetes](https://medium.com/@knoldus/using-sealed-secrets-in-kubernetes-7f7518d4c984)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [eminalemdar.medium.com: Cloud Native Secret Management with External Secrets' Operator](https://eminalemdar.medium.com/cloud-native-secret-management-with-external-secrets-operator-2912f41f9c49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/google-cloud: Handle Kubernetes Secrets the GitOps Way — Part' 1](https://medium.com/google-cloud/handle-kubernetes-secrets-the-gitops-way-part-1-7079bd8221f3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Using SSL certificates from Let’s Encrypt in your Kubernetes Ingress via cert-manager 🌟](https://medium.com/flant-com/cert-manager-lets-encrypt-ssl-certs-for-kubernetes-7642e463bbce)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Encrypting the certificate for Kubernetes (Let’s Encrypt) 🌟](https://medium.com/avmconsulting-blog/encrypting-the-certificate-for-kubernetes-lets-encrypt-805d2bf88b2a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [betterprogramming.pub: Kubernetes and SSL Certificate Management 🌟](https://betterprogramming.pub/kubernetes-and-ssl-certificate-management-5f6a4b6f5ae9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Automate Certificate Management In Kubernetes Using Cert-Manager](https://faun.pub/automate-certificate-management-in-kubernetes-using-cert-manager-d0745e5c7757)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@knoldus: Configure SSL certificate with cert-manager on Kubernetes](https://medium.com/@knoldus/configure-ssl-certificate-with-cert-manager-on-kubernetes-e5ca8a804e16)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: Automated DNS/TLS with External DNS & LetsEncrypt on' Kubernetes](https://blog.devgenius.io/automated-dns-tls-with-external-dns-letsencrypt-on-kubernetes-6f4f41827df9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Let’s encrypt and CertManager](https://faun.pub/lets-encrypt-and-certmanager-aa88775730b8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armin.su: SSL certificates from Let’s Encrypt for Kubernetes Private Ingress' via Terraform](https://armin.su/ssl-certificates-from-lets-encrypt-for-kubernetes-private-ingress-via-terraform-c9f595ee65fa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [betterprogramming.pub: Kubernetes Authentication Sidecars: A Revelation' in Microservice Architecture](https://betterprogramming.pub/kubernetes-authentication-sidecars-a-revelation-in-microservice-architecture-12c4608189ab)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: SSO Authentication for Applications in Kubernetes](https://blog.devgenius.io/sso-authentication-for-applications-in-kubernetes-aedc3c189d89)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [imanishchaudhary.medium.com: Securing Kubernetes Dashboards: SSO Authentication' and RBAC Implementation with Okta and OAuth2 Proxy](https://imanishchaudhary.medium.com/secure-kubernetes-dashboards-with-sso-authentication-using-okta-oauth2-proxy-9e52189e9749)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Configure RBAC in Kubernetes Like a Boss 🌟](https://medium.com/trendyol-tech/configure-rbac-in-kubernetes-like-a-boss-665e2a8665dd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes RBAC Permission Manager 🌟](https://toolbox.kali-linuxtr.net/kubernetes-rbac-permission-manager.tool)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/devops-mojo: Kubernetes — Role-Based Access Control (RBAC) Overview](https://medium.com/devops-mojo/kubernetes-role-based-access-control-rbac-overview-introduction-rbac-with-kubernetes-what-is-2004d13195df)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft-sh.medium.com: 10 Essentials for Kubernetes Access Control](https://loft-sh.medium.com/10-essentials-for-kubernetes-access-control-a67ae72977dd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sumanthkumarc.medium.com: Kubernetes RBAC — Update default ClusterRoles' without editing them](https://sumanthkumarc.medium.com/kubernetes-rbac-update-default-clusterroles-without-editing-them-ef206254e0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Assign permissions to an user in Kubernetes. An overview of RBAC-based' AuthZ in k8s 🌟](https://faun.pub/assign-permissions-to-an-user-in-kubernetes-an-overview-of-rbac-based-authz-in-k8s-7d9e5e1099f1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@badawekoo: Using RBAC in Kubernetes for authorization-Complete' Demo-Part 1](https://medium.com/@badawekoo/using-rbac-in-kubernetes-for-authorization-complete-demo-part-1-83f0a1fb8f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@15daniel10: YOYO attack on a K8S cluster](https://medium.com/@15daniel10/yoyo-attack-on-a-k8s-cluster-102bc1d5ca3e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@danielepolencic: How does RBAC work in kubernetes 🌟](https://medium.com/@danielepolencic/how-does-rbac-work-in-kubernetes-d50dd34771ca)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dominik-tornow.medium.com: Inside Kubernetes RBAC](https://dominik-tornow.medium.com/inside-kubernetes-rbac-9988b08a738a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jtdv01: Kubernetes Authorization and Role Based Access Controls' 🌟](https://medium.com/@jtdv01/kubernetes-authorization-and-role-based-access-controls-ca0b7acc17a4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Give Users and Groups Access to Kubernetes Cluster Using RBAC](https://faun.pub/give-users-and-groups-access-to-kubernetes-cluster-using-rbac-b614b6c0b383)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@danielepolencic: AWS IAM Roles for service accounts for on-prem' clusters](https://medium.com/@danielepolencic/binding-aws-iam-roles-to-kubernetes-service-account-for-on-prem-clusters-b8bac41f269d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/andcloudio: Setting up Authentication and RBAC Authorization' in Kubernetes](https://medium.com/andcloudio/creating-authentication-and-authorization-in-kubernetes-c6c5f0f1d2ad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@mehmetodabashi: Authentication and Authorization in Kubernetes:' Client Certificates and Role Based Access Control (RBAC)](https://medium.com/@mehmetodabashi/authentication-and-authorization-in-kubernetes-client-certificates-and-role-based-access-control-d4e98a3c1098)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@brunoolimpio: Kubernetes DeepDive — Parte 2 - Kubernetes RBAC' and more... | Bruno Olimpio](https://medium.com/@brunoolimpio/kubernetes-deepdive-parte-2-a65ffdce596d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.styra.com: Why RBAC is not enough for kubernetes security 🌟🌟](https://blog.styra.com/blog/why-rbac-is-not-enough-for-kubernetes-api-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/dynatrace-engineering: Kubernetes Security Best Practices Part' 2: Network Policies](https://medium.com/dynatrace-engineering/kubernetes-security-best-practices-part-2-network-policies-405b36ed9d94)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@cloud_tips: Kubernetes Security Best Practices](https://medium.com/@cloud_tips/kubernetes-security-best-practices-ea1e3913c001)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [magalix.com: kubernetes authentication 🌟](https://www.magalix.com/blog/kubernetes-authentication)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [magalix.com: kubernetes authorization 🌟](https://www.magalix.com/blog/kubernetes-authorization)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [lisowski0925.medium.com: Using Kubernetes Certificate Signing Requests and' RBAC for User Authentication and Authorization](https://lisowski0925.medium.com/using-kubernetes-csrs-and-rbac-for-cluster-user-authentication-and-authorization-9df5498655cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes Authentication and Authorization with X509 client certificates](https://medium.com/@sureshpalemoni/kubernetes-authentication-and-authorization-with-x509-client-certificates-edbc3517c10)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [stackoverflow: Accessing the Kubernetes REST end points using bearer token](https://stackoverflow.com/questions/56214715/accessing-the-kubernetes-rest-end-points-using-bearer-token)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ibrahims.medium.com: Security Context — Kubernetes](https://ibrahims.medium.com/security-context-kubernetes-9672ae2380f9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Securing Kubernetes Dashboard on EKS with Pomerium](https://medium.com/dev-genius/securing-kubernetes-dashboard-on-eks-with-pomerium-e98c47610e2f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mahira-technology.medium.com: Kubernetes Secrets Management: Level Up with' External Secrets Operator](https://mahira-technology.medium.com/kubernetes-secrets-management-level-up-with-external-secrets-operator-ed7d32df2189)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.lightspin.io: NGINX Custom Snippets CVE-2021-25742](https://blog.lightspin.io/nginx-custom-snippets-cve-2021-25742)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## API Access Protection

### Teleport Access Control

  - **(2021)** [goteleport.com: Kubernetes API Access Security Hardening](https://goteleport.com/blog/kubernetes-api-access-security) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Assesses security postures for Kube-API exposure, outlining standard secure practices including zero-trust access, bastions, detailed telemetry streams, and short-lived credentials.
## Architecture

### Microservices

#### Application Lifecycle

  - **(2022)** [itnext.io: Journey Of A Microservice Application In The Kubernetes World 🌟](https://itnext.io/journey-of-a-microservice-application-in-the-kubernetes-world-6abd625c60fe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Traces the structural lifecycle of a containerized microservice traversing deployment pipelines, service routing, and load balancing configurations. Provides practical insights into configuring readiness/liveness probes, autoscaling parameters, and ingress rules. Essential reference for microservice platform standardization.
## CKS Certification Study Guides

### Cluster Lifecycle Security

  - **(2020)** [==github.com/stackrox: Certified Kubernetes Security Specialist Study Guide' 🌟==](https://github.com/stackrox/Kubernetes_Security_Specialist_Study_Guide) <span class='md-tag md-tag--info'>⭐ 429</span> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive community study handbook for the Linux Foundation CKS exam, detailing system hardening, threat mitigation, microservice security policies, and runtime compliance enforcement.
## CNI Network Vulnerabilities

### Network Penetration Testing

  - **(2020)** [cyberark.com: Attacking Kubernetes Clusters Through Your Network Plumbing: Part 1](https://www.cyberark.com/resources/threat-research-blog/attacking-kubernetes-clusters-through-your-network-plumbing-part-1?utm_sq=goa40uvlx1) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Delves into how container network interfaces (CNIs) and underlying network configurations can be targets for spoofing, route injection, and MITM attacks within shared Kubernetes clusters.
## CVE Analysis

### Network Vulnerabilities

  - **(2020)** [empresas.blogthinkbig.com: Descubierta una vulnerabilidad en Kubernetes que permite acceso a redes restringidas (CVE-2020-8562)](https://empresas.blogthinkbig.com/descubierta-vulnerabilidad-kubernetes-permite-acceso-redes-restringidas-cve-2020-8562) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes CVE-2020-8562, a vulnerability allowing path-traversal/access bypass to internal restricted subnets through the Kubernetes API server, discussing standard mitigation strategies.
## Case Studies

### Historical Exploit Analysis

  - **(2021)** [thenewstack.io: Kubernetes: An Examination of Major Attacks 🌟](https://thenewstack.io/kubernetes-an-examination-of-major-attacks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Conducts retrospective post-mortems on major real-world Kubernetes security incidents, tracing malicious lateral movements, coin-miner deployments, and critical data breaches back to root posture issues.
## Cloud Native Networking

### Network Policies

#### Calico and Tigera Security

  - **(2020)** [tigera.io: Kubernetes security policy design: 10 critical best practices 🌟](https://www.tigera.io/blog/kubernetes-security-policy-10-critical-best-practices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A strategic framework for designing cluster-wide network policies, using tiered structures, explicit default-deny states, and labeling schemas to scale security dynamically.
#### Secure CNI Implementation

  - **(2021)** [itnext.io: How-To: Kubernetes Cluster Network Security 🌟](https://itnext.io/how-to-kubernetes-cluster-network-security-f19bc99161f5) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical tutorial covering secure network policy design. Guides readers through limiting pod egress/ingress, utilizing global network policies, and implementing namespaces as security perimeters.
## Cloud Native Security

### The 4Cs of Cloud Native Security

  - **(2020)** [kubernetes.io: Cloud native security for your clusters](https://kubernetes.io/blog/2020/11/18/cloud-native-security-for-your-clusters) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An authoritative review of the '4C's of Cloud Native Security' (Cloud, Cluster, Container, Code). Explains how defense-in-depth principles apply across all layers of the cloud-native application stack.
## Cluster Hardening

### Infrastructural Protection

  - **(2020)** [containerjournal.com: How to Secure Your Kubernetes Cluster 🌟](https://cloudnativenow.com/topics/cloudnativesecurity/how-to-secure-your-kubernetes-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Evaluates cluster configurations across storage, networking, and deployment lifecycles. Discusses the replacement of deprecated Pod Security Policies with built-in Pod Security Standards and third-party policy engines.
### Network Policies (1)

  - **(2019)** [==Kubernetes Security Best Practices 🌟==](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md#firewall-ports-fire) <span class='md-tag md-tag--info'>⭐ 2712</span> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A curated GitHub repository delineating hardened configurations for Kubernetes API servers, Kubelets, and network boundaries. It details port-level access rules, ingress/egress filtering, and cluster isolation tactics to defend against pivot attacks.
### Operational Security

  - **(2020)** [codeburst.io: 7 Kubernetes Security Best Practices You Must Follow](https://codeburst.io/7-kubernetes-security-best-practices-you-must-follow-ae32f1ed6444) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines fundamental security practices for Kubernetes workloads, focusing on enabling RBAC, using namespaces for boundary control, managing secrets securely, and upgrading Kubernetes control planes to address known CVEs.
### Runtime Secrets Scanning

  - **(2021)** [blog.gitguardian.com: Hardening Your Kubernetes Cluster - Guidelines (Pt. 2) 🌟](https://blog.gitguardian.com/hardening-your-k8s-pt-2) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The second part of a structural security guide detailing advanced settings such as RBAC limitations, audit logging targets, container engine isolation, and secrets scanning policies.
### Security Best Practices

  - **(2020)** [horovits.wordpress.com: Kubernetes Security Best Practices](https://horovits.wordpress.com/2020/07/15/kubernetes-security-best-practices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains foundational steps for securing Kubernetes API access, configuring container execution privileges, and auditing container images within CI/CD pipelines.
## Cluster Lifecycle Security (1)

### Operating System Paradigm

  - **(2020)** [thenewstack.io: How to Secure Kubernetes, the OS of the Cloud](https://thenewstack.io/how-to-secure-kubernetes-the-os-of-the-cloud) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the concept of Kubernetes operating as a cloud-native OS, presenting strategies for securing core services, container communication, and control plane boundaries.
## Cluster Misconfigurations

### Common Mistakes

  - **(2021)** [fairwinds.com: Discover the Top 5 Kubernetes Security Mistakes You're (Probably) Making](https://www.fairwinds.com/blog/top-5-kubernetes-security-mistakes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identifies common configuration mistakes like neglected CPU/memory limits, running containers as root, and using unvalidated base images, offering immediate structural remedies.
## Defense in Depth

### Cluster Hardening (1)

  - **(2020)** [thenewstack.io: Defend the Core: Kubernetes Security at Every Layer](https://thenewstack.io/defend-the-core-kubernetes-security-at-every-layer) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides an architectural approach to layered container defense. Examines the integration of secure hardware baselines, API rate limiting, network-level firewalls, and runtime analysis agents.
## Identity and Access Management

### SSO and OIDC Configuration

  - **(2020)** [talkingquickly.co.uk: Kubernetes Single Sign On - A detailed guide 🌟](http://www.talkingquickly.co.uk/kubernetes-sso-a-detailed-guide) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to integrate Kubernetes API access with external identity providers (OIDC) to enable secure Single Sign-On (SSO) and unify role assignments across developers.
## Industry Reports

### Archived Market Trends

  - **(2021)** [redhat.com: State of Kubernetes Security Report - Spring 2021 (PDF) 🌟](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en.pdf) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive market study from Spring 2021 highlighting systemic security incidents and detailing key threat factors, infrastructure risks, and tooling choices among enterprise development teams.
### Enterprise Security Trends

  - **(2021)** [redhat.com: The State of Kubernetes Security](https://www.redhat.com/en/blog/state-kubernetes-security) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's analysis of container security threats, identifying key issues such as misconfigurations, unpatched vulnerabilities, and integration friction in cloud-native operational environments.
## Infrastructure

### AWS Integration

#### Networking

  - **(2024)** [EC2 ENI and IP Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Critical hardware reference outlining IP address and Elastic Network Interface (ENI) allocation limits per EC2 instance type. This heavily dictates pod density capabilities when utilizing the VPC CNI plug-in. Platform architects use this data to calculate scaling limits and avoid network exhaustion.
## Kubernetes Platform Engine

### Cluster Installation and Hardening

#### Infrastructure Provisioning

  - **(2020)** [thenewstack.io: Best Practices for Securely Setting up a Kubernetes Cluster](https://thenewstack.io/best-practices-for-securely-setting-up-a-kubernetes-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Breaks down secure cluster bootstrapping steps, including encrypting secrets at rest in etcd, enabling control plane mutual TLS (mTLS), and minimizing public API endpoint exposure.
### Container Runtimes

#### Runtime Isolation

  - **(2020)** [thenewstack.io: A Security Comparison of Docker, CRI-O and Containerd 🌟](https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compares the security architecture and attack surfaces of primary container runtimes: Docker, CRI-O, and Containerd. Discusses rootless execution, sandboxed runtimes (Kata, gVisor), and syscall filtering.
## Networking (1)

### CNI

#### Cilium

  - **(2026)** [cilium.io 🌟](https://cilium.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main website for Cilium, the industry-standard networking, security, and observability engine powered by eBPF. Eliminates routing performance penalties and delivers deep API metrics.
## Networking and Security

### Security Compliance

#### CIS Benchmarks

  - **(2026)** [==kube-bench 🌟==](https://github.com/aquasecurity/kube-bench) <span class='md-tag md-tag--info'>⭐ 8078</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry standard tool to check whether Kubernetes clusters are deployed securely according to the Center for Internet Security (CIS) benchmarks. Can be run inside container workloads or directly on node hosts, outputting detailed reports identifying API, TLS, and permissions vulnerabilities.
## Observability and Monitoring

### Runtime Security

#### Falco and K3s Audit Logging

  - **(2021)** [Analyze Kubernetes Audit logs using Falco 🌟](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates how to pipe Lightweight Kubernetes (K3s) API server audit logs directly into CNCF Falco. Perfect for resource-constrained edges and automated home lab deployments.
#### Security Industry Analysis

  - **(2021)** [infoworld.com: The race to secure Kubernetes at run time](https://www.infoworld.com/article/2270825/the-race-to-secure-kubernetes-at-runtime.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents the evolution of runtime threat defense in cloud-native platforms, discussing the industry shift toward kernel-level security telemetry leveraging eBPF technology.
#### Sysdig and Falco Audit Integration

  - **(2020)** [sysdig.com: Getting started with Kubernetes audit logs and Falco 🌟](https://www.sysdig.com/blog/kubernetes-audit-log-falco) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to integrate Kubernetes API audit logs with CNCF Falco to capture real-time control plane actions and alert on malicious requests, credential abuse, or abnormal operational API traffic.
### eBPF Runtime Enforcement

#### Tetragon Platform

  - **(2022)** [==Tetragon (Cilium)==](https://github.com/cilium/tetragon) <span class='md-tag md-tag--info'>⭐ 4749</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An eBPF-powered security observability and runtime enforcement platform. It monitors and blocks system events at the kernel level, providing granular process execution, network activity, and file system audit streams with zero container overhead.
## Penetration Testing

### Security Operations

  - **(2020)** [youtube: Kubernetes Security: Attacking and Defending K8s Clusters - by Magno Logan](https://www.youtube.com/watch?v=OOHmg1J_8ck&ab_channel=RedTeamVillage) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical, demonstration-heavy guide outlining attack-and-defend methodologies for production clusters. Demonstrates common configuration exploits and dynamic remediation.
## Pod Privilege Escalation

### Vulnerability Exploitation

  - **(2020)** [labs.bishopfox.com: Bad Pods: Kubernetes Pod Privilege Escalation 🌟](https://bishopfox.com/blog/kubernetes-pod-privilege-escalation) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly cited technical analysis demonstrating how misconfigured container host namespaces, capabilities, and volume mounts can be exploited to escape container boundaries and gain full host-level access.
## Policy-as-Code

### Kyverno Administration

  - **(2020)** [kyverno.io 🌟](https://kyverno.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kyverno is a declarative Kubernetes-native policy engine. Designed specifically for Kubernetes, it simplifies policy management by allowing administrators to validate, mutate, and generate resources without writing complex Rego code.
### Kyverno Rules and Policies

  - **(2020)** [kyverno.io/policies 🌟](https://kyverno.io/policies) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official catalog of Kyverno policies, providing ready-to-deploy manifests for Pod Security standards, multi-tenant workspace isolation, label validation, and compliance auto-generation.
## RBAC and Authorization

### Privilege Escalation

  - **(2020)** [jeffgeerling.com: Everyone might be a cluster-admin in your Kubernetes cluster](https://www.jeffgeerling.com/blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates RBAC misconfigurations and overly permissive default service accounts that elevate microservice workloads to cluster-admin privileges. It provides actionable remediation strategies for locking down namespace-bound credentials.
## Risk Analysis and Auditing

### Threat Vector Modeling

  - **(2020)** [tldrsec.com: Risk8s Business: Risk Analysis of Kubernetes Clusters 🌟](https://tldrsec.com/?404=%2Fguides%2Fkubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive vulnerability catalog and risk analysis guide highlighting exploitation pathways in typical cluster deployments. Highlights the security impacts of insecure volume mounts and metadata service access.
## Secrets Management

### HashiCorp Vault Integration

  - **(2020)** [learn.hashicorp.com: Integrate a Kubernetes Cluster with an External Vault 🌟](https://developer.hashicorp.com/vault/tutorials/kubernetes-introduction/kubernetes-external-vault) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical implementation guide showcasing how to leverage the HashiCorp Vault Agent Injector sidecar to dynamically inject secrets directly into application pods via in-memory tmpfs mounts.
## Security

### Access Control

#### API Access

  - **(2024)** [kubernetes.io: Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official task-oriented guide illustrating the safe initialization of connections directly to the Kubernetes API server. It highlights proxying patterns, kubectl integration, and direct API calls via transport-layer security (TLS). Essential for developers automating low-level operations within controlled environments.
#### Authentication

  - **(2024)** [kubernetes.io: Authenticating](https://kubernetes.io/docs/reference/access-authn-authz/authentication) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The core official reference for understanding user and service account authentication mechanisms in Kubernetes. It reviews client certificates, bearer tokens, and OIDC federation protocols. This architectural baseline explains how kube-apiserver validates identity requests securely.
#### Cluster Access

  - **(2024)** [kubernetes.io: Accesing Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how developers and administrators access remote clusters using credential files (kubeconfigs). This documentation reviews contextual switching, multi-cluster management, and local proxy patterns. It serves as a foundational step for secure local engineering workflows.
#### Custom Authentication

  - **(2023)** [Implementing a custom Kubernetes authentication method](https://learnkube.com/kubernetes-custom-authentication) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Provides a technical blueprint for implementing bespoke authentication strategies using webhook token authentication. It explains the integration of custom identity backends with the kube-apiserver lifecycle. Recommended for highly specialized security architectures with legacy SSO restrictions.
#### RBAC

  - **(2022)** [engineering.dynatrace.com: Kubernetes Security Best Practices -Part 1: Role Based Access Control (RBAC)](https://www.dynatrace.com/news/engineering) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into Kubernetes Role-Based Access Control (RBAC) mechanisms and configuration patterns. The guide stresses the architectural importance of the Principle of Least Privilege, outlining best practices for defining Roles and ClusterRoles. Practical mitigation strategies focus on auditing wildcard permissions to avoid escalation risks.
#### kubectl Authentication

  - **(2020)** [kubernetes login](https://blog.christianposta.com/kubernetes/logging-into-a-kubernetes-cluster-with-kubectl)  <span class='md-tag md-tag--info'>[LEGACY]</span> — A legacy-focused technical exploration explaining the login process flow through kubectl. This article breaks down the historical and contemporary mechanics of authentication helpers and tokens. Ideal for engineers seeking to demystify credential caching behaviors.
### Application Security

#### Client Security

  - **(2022)** [curity.io: Client Security](https://curity.io/resources/client-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on security patterns when structuring application clients that interface with identity ecosystems. Covers patterns like Token Handlers and Backend-for-Frontend (BFF) to safely abstract tokens away from client browsers or apps. Reduces target exposures to common cross-site scripting risks.
### Architecture (1)

#### DevSecOps

  - **(2022)** [thenewstack.io: Securing Kubernetes in a Cloud Native World](https://thenewstack.io/securing-kubernetes-in-a-cloud-native-world)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This technical analysis explores how security shifts within high-velocity cloud-native deployments. Outlines strategies for managing immutable infrastructure, dynamic policy updates, and zero-trust routing. Strongly advocates for shifting security controls left and using automated gating engines.
#### Future Trends

  - **(2022)** [thenewstack.io: Basic Principles Key to Securing Kubernetes’ Future](https://thenewstack.io/key-basic-principles-to-secure-kubernetes-future)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines long-term trends in cloud-native security, arguing for declarative and immutable configurations as the main vector of defense. Synthesizes principles of software supply chain verification (such as Sigstore/Cosign integration) and automated drift detection. Vital for architects planning 3-to-5 year container strategies.
### Audit

#### Configuration Assessment

  - **(2023)** [securitycafe.ro: A COMPLETE KUBERNETES CONFIG REVIEW METHODOLOGY](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exhaustive, step-by-step methodology for auditing the entire configuration footprint of Kubernetes environments. Provides structural steps for scanning RBAC bindings, assessing cluster configuration parameters, and scanning host node vulnerabilities. Essential checklist for compliance officers and security auditors.
### Best Practices

#### General Hardening

  - **(2024)** [armosec.io: Kubernetes Security Best Practices: Definitive Guide](https://www.armosec.io/blog/kubernetes-security-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exhaustive technical blueprint emphasizing end-to-end cloud-native system security. It details critical hardening strategies including image scanning, continuous compliance auditing, and secure runtime boundaries. Modern operators leverage these concepts to build proactive defensive postures across hybrid clusters.
  - **(2023)** [thenewstack.io: 6 Kubernetes Security Best Practices 🌟](https://thenewstack.io/6-kubernetes-security-best-practices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A baseline architectural guide covering foundational security principles in Kubernetes. It focuses on isolating workloads, enabling network policies, and minimizing container privileges. Real-world implementation highlights the mitigation of broad blast radii by enforcing namespace segregation.
  - **(2023)** [spectrocloud.com: Kubernetes security best practices: 5 easy ways to cut risk](https://www.spectrocloud.com/blog/kubernetes-security-best-practices-5-easy-ways-to-cut-risk)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines five high-impact security wins to drastically lower cluster risk vectors. Key practices include restrictive network boundary controls, cluster-wide image pinning, and utilizing immutable root filesystems. These pragmatically reduce immediate exposure surfaces for standard multi-tenant setups.
### Cloud Security

#### AWS EKS Network

  - **(2024)** [Security Group Rules EKS](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS configuration documentation detailing the network security boundaries for Amazon EKS clusters. It defines minimal requirements for control-plane-to-node communication over secure ports. This ensures highly restrictive ingress/egress patterns in security groups.
### Cluster Hardening (2)

#### Audit Logs

  - **(2022)** [blog.gitguardian.com: Kubernetes Hardening Tutorial Part 3: Authn, Authz, Logging & Auditing](https://dev.to/gitguardian/kubernetes-hardening-tutorial-part-3-authn-authz-logging-auditing-3fec)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part three of the GitGuardian series, focusing on authentication, authorization, logging, and audit tracking. Demonstrates how to design granular RBAC policies and enable cluster audit logs to detect security anomalies. Essential for establishing reliable forensic trails.
#### Best Practices (1)

  - **(2022)** [cast.ai: Kubernetes Security: 10 Best Practices from the Industry and Community 🌟](https://cast.ai/blog/kubernetes-security-10-best-practices)  <span class='md-tag md-tag--info'>[LEGACY]</span> — Consolidates ten core security practices derived from cloud-native community patterns and expert input. Discusses API server hardening, encryption of secrets at rest in etcd, and continuous vulnerability verification. Provides a clear roadmap for migrating legacy infrastructure securely into Kubernetes.
  - **(2022)** [dev.to/aws-builders: Best Practices for Securing Kubernetes Deployments 🌟](https://dev.to/aws-builders/best-practices-for-securing-kubernetes-deployments-1jg6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents an action-oriented best practice matrix covering cluster configuration and pod safety profiles. Details etcd encryption setups, secure secrets distribution patterns, and implementing standard Pod Security Admission policies. Highly recommended for establishing cluster baselines.
#### Deployment Security

  - **(2022)** [armosec.io: How to Secure Deployments in Kubernetes? 🌟](https://www.armosec.io/blog/secure-kubernetes-deployment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An operational guide on implementing Pod Security Standards (PSS) within modern clusters. Provides precise configurations for configuring read-only root filesystems, restricting Linux capability escalation, and rejecting root execution. Helps secure standard application manifests against common run-time threat models.
#### Pod Security

  - **(2022)** [dev.to/thenjdevopsguy: Securing Kubernetes Pods For Production Workloads](https://dev.to/thenjdevopsguy/securing-kubernetes-pods-for-production-workloads-51oh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on runtime container hardening for critical production clusters. Provides examples of setting up restricted securityContext parameters, dropping raw Linux capabilities, and activating seccomp profiles. Ensures configurations restrict exploitation should container escape vulnerabilities emerge.
#### Standard Checklists

  - **(2023)** [kubernetes.io: Security Checklist 🌟🌟](https://kubernetes.io/docs/concepts/security/security-checklist) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official security checklist published by upstream Kubernetes maintainers. It serves as an authoritative map for hardening cluster networks, applying role access structures, and validating runtimes. Essential baseline documentation for cloud infrastructure engineers.
### Deployment Security (1)

#### Hardening

  - **(2023)** [semaphoreci.com: Secure Your Kubernetes Deployments](https://semaphore.io/blog/kubernetes-deployments)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on incorporating shift-left security strategies directly into the CI/CD deployment pipeline. It details how to leverage static manifest analysis, configuration linters, and runtime context constraints. This is essential for preventing misconfigured workloads from reaching production environments.
### DevSecOps (1)

#### CICD Pipeline Security

  - **(2022)** [infoworld.com: 10 steps to automating security in Kubernetes pipelines](https://www.infoworld.com/article/2258136/10-steps-to-automating-security-in-kubernetes-pipelines.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A ten-step technical blueprint focused on integrating security scanners directly into automated CI/CD deployment pipelines. Covers static application security testing (SAST), secrets detection, and manifest scanning before changes reach staging or production clusters. Outlines shift-left strategies to mitigate misconfiguration deployment risks.
#### Continuous Security

  - **(2022)** [collabnix.com: Applying DevSecOps Practices to Kubernetes](https://collabnix.com/applying-devsecops-practices-to-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the technical implementation of DevSecOps pipelines targeting Kubernetes applications. Discusses how to configure automated feedback loops between static manifest linters, container register vulnerability databases, and runtime audit monitors. Crucial for scaling secure delivery pipelines.
#### Developer Guidance

  - **(2022)** [dev.to/pavanbelagatti: Kubernetes Security Best Practices For Developers](https://dev.to/pavanbelagatti/kubernetes-security-best-practices-for-developers-2b92)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Translates complex cluster security profiles into digestible concepts tailored directly for application developers. Focuses on safe manifest construction, secret handling, and using non-root base images. Encourages safe development workflows to eliminate security issues before code merges.
### Fundamentals

#### Concepts

  - **(2022)** [itnext.io: Introduction to Kubernetes Security for Security Professionals](https://itnext.io/introduction-to-kubernetes-security-for-security-professionals-a61b424f7a2a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An entry point resource for security practitioners pivoting from virtual machines or bare-metal servers into Kubernetes environments. Explains standard architectural paradigms like Pods, Namespaces, Service Accounts, and Admission Controllers. Focuses on building a coherent threat modeling mental map.
  - **(2022)** [dev.to/mattiasfjellstrom: Kubernetes-101: Security concepts](https://dev.to/mattiasfjellstrom/kubernetes-101-security-concepts-2f4f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory security conceptual guide reviewing isolation techniques like Linux namespaces, cgroups, and capabilities. Correlates these kernel-level tools to upstream abstraction parameters in standard Pod specs. Provides a concise, high-density primer on basic defense constructs.
#### Threat Modeling

  - **(2022)** [blog.gitguardian.com: Hardening Your Kubernetes Cluster - Threat Model (Pt. 1) 🌟🌟](https://blog.gitguardian.com/hardening-your-k8-pt-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of a tutorial series focusing on threat modeling within Kubernetes systems. Outlines typical attack surface definitions across components like API endpoints, etcd systems, and workers. Aids engineering teams in establishing defense boundaries.
### Hardening Standards

#### Government Guidelines

  - **(2022)** [armosec.io: NSA & CISA Kubernetes Hardening Guide – what is new with version 1.1](https://www.armosec.io/blog/nsa-cisa-kubernetes-hardening-guide)  <span class='md-tag md-tag--info'>[LEGACY]</span> — Details updates in version 1.1 of the NSA-CISA Kubernetes Hardening Guide. Highlights transition criteria from deprecated PodSecurityPolicies to Pod Security Standards, alongside advice on checking third-party integrations. Helps teams stay aligned with current guidance.
  - **(2021)** [thenewstack.io: The NSA Can Help Secure Your Kubernetes Clusters](https://thenewstack.io/the-nsa-can-help-you-secure-your-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates the joint security guidance on Kubernetes hardening issued by the NSA and CISA. Translates government recommendations into actionable steps for enterprise IT administrators. Focuses on separation of credentials and configuring audit pathways.
  - **(2021)** [therecord.media: NSA, CISA publish Kubernetes hardening guide 🌟🌟](https://therecord.media/nsa-cisa-publish-kubernetes-hardening-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed breakdown of the NSA/CISA Kubernetes Hardening Guide. Emphasizes container sandboxing, running applications with minimal privilege bounds, and dividing networks to limit damage. A vital reference point for regulatory compliance projects.
  - **(2021)** [infoq.com](https://www.infoq.com/news/2021/09/kubernetes-hardening-guidance)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores key recommendations from CISA and the NSA regarding cluster infrastructure protection. Demystifies technical methods for managing root filesystems, authenticating platform API requests, and using logging setups to trace lateral movement.
  - **(2021)** [thenewstack.io: NSA on How to Harden Kubernetes](https://thenewstack.io/nsa-on-how-to-harden-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical review focusing on the security configurations defined within the NSA hardening guides. Covers container escape avoidance, using read-only structures, and setting up logging patterns. Beneficial for system engineers translating recommendations to production setups.
### IAM

#### Authentication and Authorization

  - **(2022)** [dev.to/thenjdevopsguy: The 4 C’s Of Kubernetes Security](https://dev.to/thenjdevopsguy/the-4-cs-of-kubernetes-security-3i9e) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates enterprise patterns for integrating Kubernetes Role-Based Access Control (RBAC) with corporate directory systems (OIDC, Active Directory). Examines tools like Dex to implement single sign-on (SSO) strategies across multi-cluster environments. Essential reading for cluster operations scaling across departments.
#### SSO

  - **(2022)** [dev.to/gabrielbiasi: Automatic SSO in Kubernetes workloads using a sidecar container](https://dev.to/gabrielbiasi/automatic-sso-in-kubernetes-workloads-using-a-sidecar-container-3752)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines an automated SSO sidecar integration pattern inside Kubernetes pods, abstracting authentication logic away from application-level containers. Details OAuth token management and redirect intercept strategies executed transparently at the pod level. Simplifies identity integration across multiple microservices.
### Identity and Access

#### AWS IRSA

##### Hybrid Cloud

  - **(2022)** [dev.to: Binding AWS IAM roles to Kubernetes Service Account for on-prem clusters | Daniele Polencic 🌟](https://dev.to/danielepolencic/binding-aws-iam-roles-to-kubernetes-service-account-for-on-prem-clusters-1icc) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Highlights solutions for extending AWS IAM Roles for Service Accounts (IRSA) configurations into on-premises Kubernetes clusters. Solves the hybrid identity challenge by utilizing OIDC federated discovery documents on local nodes.
#### Authentication (1)

##### Legacy Tools

  - **(2020)** [github.com/dvob/k8s-s2s-auth: Kubernetes Service Accounts 🌟](https://github.com/dvob/k8s-s2s-auth) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: Demonstrates internal service-to-service auth patterns utilizing raw Service Account tokens. Live Grounding: The repository has seen no recent development and is considered legacy. It is superseded by modern ephemeral TokenRequest APIs and service mesh mTLS integrations.
  - **(2023)** [learnk8s.io/authentication-kubernetes: User and workload identities in Kubernetes 🌟🌟🌟](https://learnkube.com/authentication-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A deep analysis of the conceptual differences between human and workload identities within Kubernetes. Details how API server authentication modules resolve internal workloads using Service Accounts, contrasting them with external OIDC providers.
  - **(2022)** [goteleport.com: A Simple Overview of Authentication Methods for Kubernetes Clusters](https://goteleport.com/blog/kube-authn-methods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synthesizes multiple Kubernetes authentication methods—including bootstrap tokens, client certificates, webhook tokens, and OIDC federation. Provides an architect-level comparison of trade-offs regarding credential life and operational complexity.
#### Cloud Integrations

##### AWS IRSA (1)

  - **(2021)** [mjarosie.github.io: IAM roles for Kubernetes service accounts - deep dive](https://mjarosie.github.io/dev/2021/09/15/iam-roles-for-kubernetes-service-accounts-deep-dive.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A thorough exploration of AWS IAM Roles for Service Accounts (IRSA). Demystifies how AWS OpenID Connect (OIDC) federation interacts with mutating admission webhooks to inject dynamic, temporary AWS STS credentials into Kubernetes pods.
#### Enterprise Authentication

  - **(2022)** [loft.sh: Kubernetes and LDAP: Enterprise Authentication for Kubernetes](https://www.vcluster.com/blog/kubernetes-and-ldap-enterprise-authentication-for-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Outlines pattern-driven integrations for bridging classic corporate LDAP servers with modern Kubernetes clusters. Focuses on identity broker abstractions like Dex to map legacy LDAP groups to Kubernetes RBAC definitions.
#### Microservice Identities

  - **(2023)** [learnk8s.io: Authentication between microservices using Kubernetes identities 🌟](https://learnkube.com/microservices-authentication-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized guide analyzing how service-to-service communication can be secured natively. It demonstrates using Kubernetes ServiceAccount tokens as cryptographic identities to authenticate microservices without external overhead. This pattern reduces dependencies on heavy service meshes for simpler deployments.
#### OIDC

##### Legacy Tools (1)

  - **(2020)** [==gini/dexter==](https://github.com/gini/dexter) <span class='md-tag md-tag--info'>⭐ 168</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: An OIDC-helper CLI tool for generating kubectl credential configurations. Live Grounding: Inactive for over 4 years; considered legacy under Nubenetes MVQ rules. It has been superseded by tools like kubelogin.
##### OAuth2 Proxy

  - **(2021)** [geek-cookbook.funkypenguin.co.nz: Using OAuth2 proxy for Kubernetes Dashboard](https://geek-cookbook.funkypenguin.co.nz/recipes/kubernetes/oauth2-proxy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A configuration guide describing how to wrap the Kubernetes Dashboard and sensitive internal APIs with oauth2-proxy, enabling secure OIDC integrations and SSO workflows.
  - **(2024)** [OpenID Connect](https://openid.net) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official specifications for OpenID Connect, the dominant federation protocol for Kubernetes authentication. Implementing OIDC enables modern clusters to offload authentication to external identity providers like Okta, Keycloak, or Microsoft Entra ID. This standardizes identity tokens globally across decentralized services.
#### RBAC (1)

##### Legacy Tools (2)

  - **(2020)** [==Krane 🌟==](https://github.com/appvia/krane) <span class='md-tag md-tag--info'>⭐ 740</span> <span class='md-tag md-tag--warning'>[RUBY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: An open-source Kubernetes RBAC static analysis tool designed to identify risky roles, cluster roles, and broad resource access configurations. Live Grounding: The repository is archived and inactive for over 4 years. While the structural rules engine remains historically valuable, it does not support modern Kubernetes RBAC security vectors.
  - **(2019)** [==github.com/clvx/k8s-rbac-model: Kubernetes RBAC Model==](https://github.com/clvx/k8s-rbac-model) <span class='md-tag md-tag--info'>⭐ 26</span> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: A conceptual visualization framework for modeling Kubernetes RBAC policies. Live Grounding: The project has seen zero updates in over 5 years. Deprioritized under MVQ rules due to structural obsolescence against modern apiGroups.
##### Security Auditing

  - **(2022)** [raesene.github.io: Auditing RBAC - Redux](https://raesene.github.io/blog/2022/08/14/auditing-rbac-redux) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highly detailed assessment of tools and manual approaches used to audit RBAC permissions. Looks at the attack surface exposed by privileged service accounts and API server access loopholes, providing concrete defensive guidance.
  - **(2026)** [rbac.dev 🌟🌟🌟](https://rbac.dev)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated directory of tools, templates, and best practices for Kubernetes RBAC configurations. Serves as an essential reference for engineers establishing zero-trust access boundaries.
  - **(2023)** [devopscube.com: How To Create Kubernetes Service Account For API Access](https://devopscube.com/kubernetes-api-access-service-account)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical tutorial focused on provisioning Kubernetes Service Accounts for targeted API server access. Walks through credential auto-generation constraints, manifesting corresponding API access boundaries, and constructing secure automated CI/CD pipelines.
  - **(2023)** [learnk8s.io: Limiting access to Kubernetes resources with RBAC 🌟🌟🌟](https://learnkube.com/rbac-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A rigorous deep-dive into resource constraints using RBAC. Demonstrates how to write custom policies to isolate network endpoints, restrict API-driven actions, and test permissions safely using `kubectl auth can-i`.
  - **(2022)** [loft.sh: Kubernetes RBAC: Basics and Advanced Patterns](https://www.vcluster.com/blog/kubernetes-rbac-basics-and-advanced-patterns) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deconstructs advanced RBAC patterns, focusing on namespace isolation, virtual cluster (vcluster) control planes, and resolving performance regressions associated with large-scale policy databases.
  - **(2022)** [marcusnoble.co.uk: Restricting cluster-admin Permissions](https://marcusnoble.co.uk/2022-01-20-restricting-cluster-admin-permissions) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines security risks associated with widespread `cluster-admin` usage. Proposes strategies to design specialized roles with precise apiGroup restrictions to establish guardrails around the control plane.
  - **(2022)** [anaisurl.com: RBAC Explained with Examples 🌟](https://anaisurl.com/kubernetes-rbac)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A visual, beginner-friendly guide dissecting RBAC mechanics in Kubernetes. Offers concrete examples of setting up specific read/write permissions for standard development teams.
  - **(2022)** [dev.to: Configure RBAC in Kubernetes Like a Boss](https://dev.to/mstryoda/configure-rbac-in-kubernetes-like-a-boss-h67)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An operational checklist and set of best practices for establishing robust, leak-proof RBAC models. Helps administrators avoid common authorization anti-patterns such as wildcards in role rules.
  - **(2022)** [youtube: Kubernetes RBAC Explained | Anton Putra 🌟](https://www.youtube.com/watch?v=iE9Qb8dHqWI)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Detailed instructional video mapping user groups and service accounts to Kubernetes resources using RBAC. Explains role-binding syntax and access validations in an intuitive, visual style.
  - **(2021)** [infracloud.io: How to setup Role based access (RBAC) to Kubernetes Cluster 🌟](https://www.infracloud.io/blogs/role-based-access-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed technical analysis of native Kubernetes Role-Based Access Control (RBAC). Explains authorization objects (Roles, ClusterRoles, and Bindings) alongside API groups to help design least-privilege structures.
#### SSO and SAML

  - **(2022)** [gravitational.com: How to Set Up Kubernetes SSO with SAML](https://goteleport.com/blog/kubernetes-sso-saml) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deconstructs the mechanics of configuring Single Sign-On (SSO) for cluster environments utilizing SAML. The guide explains authentication federation patterns, mapping identity provider attributes to Kubernetes RBAC roles. This setup ensures seamless, centralized access management for enterprise platform infrastructure.
#### Workload Identity

  - **(2021)** [linkerd.io: Using Kubernetes's new Bound Service Account Tokens for secure workload identity](https://linkerd.io/2021/12/28/using-kubernetess-new-bound-service-account-tokens-for-secure-workload-identity/index.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines Linkerd's transition to Kubernetes Bound Service Account Tokens (TokenRequest API). Explains the security benefits of using tokens containing specific audiences, node bindings, and short lifetimes to mitigate credential leakage risks.
#### Zero Trust Access

  - **(2024)** [paralus.io 🌟](https://www.paralus.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Paralus is an open-source tool for managing access to multi-cluster Kubernetes environments. Offers a centralized portal for configuring Just-In-Time (JIT) access, OIDC integration, auditing, and RBAC synchronization across cloud providers.
### Identity and Access Management (1)

#### Access Control (1)

  - [thenewstack.io: Cloud Native Identity and Access Management in Kubernetes](https://thenewstack.io/cloud-native-identity-and-access-management-in-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Examines identity federation, user access management, and internal service-to-service authentication models. Curator insight details mapping cluster roles directly to organizational single sign-on identities. Live grounding indicates that decentralized identity and modern authentication are critical to maintaining least privilege in high-scale infrastructure.
### Kubernetes Security (1)

#### Hardening (1)

  - **(2023)** [sysdig.com: Kubernetes Security Guide 🌟](https://www.sysdig.com/blog/kubernetes-security-guide) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Sysdig's comprehensive guide to securing Kubernetes platforms details a multi-layered defense strategy covering container image scanning, runtime protection, network policies, and role-based access control (RBAC). It highlights compliance mappings (such as CIS benchmarks) and operational best practices for detecting abnormal kernel system calls using eBPF-based agents.
#### Secrets Management (1)

  - **(2021)** [Hands on your first Kubernetes secrets 🌟](https://www.theodo.com/en-uk/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This hands-on tutorial guides developers through creating, decoding, and mounting native Kubernetes Secret resources within applications. It highlights base64 encoding limitations and advises on key architectural alternatives, such as HashiCorp Vault integration, Sealed Secrets, or CSI secret store drivers for production environments.
### Network Security

#### Internet Exposure

  - **(2022)** [raesene.github.io: Let's talk about Kubernetes on the Internet](https://raesene.github.io/blog/2022/07/03/lets-talk-about-kubernetes-on-the-internet) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An urgent analytical overview assessing why many Kubernetes API control planes remain directly visible on the public internet. Discusses host-level firewall configurations, securing the Kubelet interface, and utilizing private API cluster features in major cloud providers. Emphasizes basic perimeter hygiene.
#### Network Policies (2)

  - **(2024)** [Calico in EKS](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides integration of Calico as a high-performance network policy engine alongside EKS. While AWS VPC CNI handles native IP routing, Calico enforces declarative security policies. This hybrid configuration provides robust, fine-grained L3/L4 segregation across namespace borders.
  - **(2022)** [blog.gitguardian.com: Kubernetes Hardening Tutorial Part 2: Network](https://blog.gitguardian.com/kubernetes-tutorial-part-2-network)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This technical tutorial demonstrates the configuration of Kubernetes NetworkPolicies to enforce granular traffic isolation. It contrasts default-allow networking models with secure default-deny postures, providing production-ready ingress and egress manifests. Engineers will learn how to reduce lateral threat movement by restricting pod-to-pod communications.
### Offensive Security

#### Penetration Testing (1)

  - **(2022)** [tutorialboy24.blogspot.com: A Detailed Talk about K8S Cluster Security from the Perspective of Attackers (Part 2) 🌟](https://tutorialboy24.blogspot.com/2022/09/a-detailed-talk-about-k8s-cluster.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This deep technical analysis adopts an offensive security posture to highlight subtle vulnerabilities in cluster configurations. Demystifies container escape routes, RBAC over-privileging paths, and target exploration from within compromised pods. Highly valuable for red team operators and defensive engineers building detection rules.
### PKI

#### Certificate Management

  - **(2022)** [blog.alexellis.io: What if your Pods need to trust self-signed certificates?](https://blog.alexellis.io/what-if-your-pods-need-to-trust-self-signed-certificates)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on patterns for trusting self-signed or internal enterprise Root CA certificates inside dynamic pod runtimes. Demonstrates using initContainers and shared volumes to inject trust anchors clean of custom application builds. Prevents hardcoding issues across dynamic corporate multi-tenant infrastructures.
  - **(2021)** [thenewstack.io: Jetstack Secure Promises to Ease Kubernetes TLS Security](https://thenewstack.io/jetstack-secure-promises-to-ease-kubernetes-tls-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the release and architecture of Jetstack Secure, which simplifies and automates TLS lifecycle tracking via cert-manager. Explains the centralization of public key infrastructures (PKIs) across multi-cluster hybrid clouds. Prevents application downtime caused by unpredicted certificate expirations.
### PKI and Certificates

#### Conceptual

  - **(2022)** [dev.to: Kubernetes TLS, Demystified 🌟](https://dev.to/otomato_io/possible-paths-2hfc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demystifies Kubernetes TLS configurations by explaining public/private key pairs, certificate authorities, client-cert server validations, and common Ingress security setups.
#### TLS Ingress

##### Lets Encrypt

  - **(2021)** [rejupillai.com: Let’s Encrypt the Web (for free)](https://rejupillai.com/index.php/2021/03/06/configure-tls-on-gke-ingress-for-free-with-lets-encrypt)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical walk-through detailing TLS integration on a GKE Ingress controller. Guides the configuration of HTTP-01 and DNS-01 ACME validations using cert-manager, resulting in automated, free public certificates.
#### cert-manager

##### Access Control (2)

  - **(2024)** [==github.com/cert-manager: Policy Approver==](https://github.com/cert-manager/approver-policy) <span class='md-tag md-tag--info'>⭐ 90</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The cert-manager approver-policy extension code repository. Intercepts CertificateRequest resources before submission, evaluating requested commonNames, SANs, and key constraints against user-defined security guidelines.
##### Operations

  - **(2021)** [itnext.io: Upgrade Cert-Manager for Your Production Deployment Without Downtime](https://itnext.io/upgrade-cert-manager-for-your-production-deployment-without-downtime-ee5d32fabec8) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly technical guide focusing on upgrading production cert-manager instances without cluster downtime. Addresses API version deprecations, webhook migrations, and handling CRD migrations smoothly.
  - **(2026)** [==cert-manager/cert-manager==](https://github.com/cert-manager/cert-manager) <span class='md-tag md-tag--info'>⭐ 13859</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Consolidated record of the cert-manager repository, automating certificate lifecycles to guarantee encrypted transport paths between internal microservice runtimes.
  - **(2026)** [cert-manager.io 🌟](https://cert-manager.io/docs) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation portal for cert-manager, the standard tool for cloud-native PKI. Explains configuring Issuers and Certificate manifests, detailing dynamic ACME solver pipelines, Let's Encrypt integration, and automated internal trust routing.
### Platform Hardening

#### Best Practices (2)

  - **(2024)** [Kubernetes Security 101: Risks and 29 Best Practices 🌟](https://www.redhat.com/en/topics/containers/kubernetes-security)  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Essential Red Hat Security resource detailing 29 structural recommendations across the entire build, deploy, and run lifecycle. Covers vulnerability scanning, image signing, secure context configurations, and network isolation protocols.
### Pod Security (1)

#### Pod Security Policies

  - **(2022)** [Pod Security Policy (SCC in OpenShift) 🌟](https://kubernetes.io/docs/concepts/security/pod-security-policy) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Architectural comparison contrasting OpenShift Security Context Constraints (SCC) with the deprecated Kubernetes Pod Security Policy (PSP). Live Grounding confirms PSP was completely removed in Kubernetes v1.25. This reference highlights how SCC remains enterprise-stable and active for securing namespaces in Red Hat OpenShift clusters.
  - **(2021)** [rancher.com: Enhancing Kubernetes Security with Pod Security Policies, Part 1](https://www.suse.com/c/rancher_blog/enhancing-kubernetes-security-with-pod-security-policies-part-1)  <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical look at securing container runtimes using Pod Security Policies. As PSP is now deprecated and fully removed in modern Kubernetes, this guide serves as a legacy reference for older Rancher setups. It clarifies critical container capabilities, privilege escalation preventions, and namespace defaults.
  - **(2021)** [developer.squareup.com: Kubernetes Pod Security Policies (PSP)](https://developer.squareup.com/blog/kubernetes-pod-security-policies) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Legacy deep-dive exploring Square's real-world PSP architecture and rollout procedures. Note that modern engineering standards require migrating these exact controls to Pod Security Standards (PSS) or external engines like Kyverno. Essential reading to understand historical host namespaces and filesystem restrictions.
  - **(2021)** [itnext.io: Implementing a Secure-First Pod Security Policy Architecture](https://itnext.io/implementing-a-restricted-first-pod-security-policyarchitecture-af4e906593b0) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a secure-first PSP implementation strategy. In modern systems, this restricted-first paradigm must be executed via the native Pod Security Admission (PSA) controller. It guides readers on blocking privileged root escalation paths in older clusters.
### Policy and Admission Control

#### Runtime Security (1)

##### Legacy Tools (3)

  - **(2018)** [==box/kube-exec-controller==](https://github.com/box/kube-exec-controller) <span class='md-tag md-tag--info'>⭐ 126</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Controller to restrict and audit shell execution inside Kubernetes pods. Live Grounding: Inactive for over five years. Superseded by newer ephemeral container mechanics, admission controllers (OPA/Kyverno), and modern service mesh execution boundaries.
#### Validating Webhooks

  - **(2022)** [trstringer.com: Create a Basic Kubernetes Validating Webhook](https://trstringer.com/kubernetes-validating-webhook) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step technical guide for writing a custom validating admission controller webhook. Focuses on processing API requests, writing validation criteria in Go, and configuring TLS certificate pathways between the API server and the webhook pod.
### Policy and Audit

#### Manifest Auditing

  - **(2021)** [blog.frankel.ch: Learning by auditing Kubernetes manifests](https://blog.frankel.ch/learning-auditing-kubernetes-manifests)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An educational approach to understanding Kubernetes security postures through direct manifest auditing. The author walks through security context misconfigurations, detailing how over-privileged containers expose node architectures. This technique bridges the gap between passive development and active cluster security controls.
### Policy Enforcement

#### Admission Control

  - **(2022)** [Neon Mirrors: Kubernetes Policy Comparison: OPA/Gatekeeper vs Kyverno](https://kind-brown-cfb734.netlify.app/post/2021-02/kubernetes-policy-comparison-opa-gatekeeper-vs-kyverno) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural face-off evaluating Rego-based OPA/Gatekeeper and YAML-native Kyverno. Kyverno offers exceptional ease of use for native K8s manifests, while OPA provides unparalleled expressive power for cross-system policies. It helps architects choose the correct declarative policy engine for high-compliance environments.
### Runtime Security (2)

#### Ephemeral Containers

  - **(2022)** [xenitab.github.io: Kubernetes Ephemeral Container Security 🌟](https://xenitab.github.io/blog/2022/04/12/ephemeral-container-security) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores security boundaries regarding ephemeral debugging containers, analyzing potential escalation threats through 'kubectl debug'. Highlights how improper RBAC permissions on debugging tools can expose the underlying host or container namespace. Outlines defensive constraints like restricting hostIPC and hostPID mappings.
#### eBPF

  - **(2021)** [developers.redhat.com: Secure your Kubernetes deployments with eBPF](https://developers.redhat.com/articles/2021/12/16/secure-your-kubernetes-deployments-ebpf) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details how eBPF (Extended Berkeley Packet Filter) technology shifts the runtime security paradigm away from heavy, sidecar-based observability architectures. Demonstrates writing and attaching kernel sandboxed utilities to track execution and networking footprints with minimal CPU overhead. Crucial reading for high-scale, security-conscious platform teams.
#### eBPF and Cilium

  - **(2021)** [isovalent.com: Detecting a Container Escape with Cilium and eBPF](https://isovalent.com/blog/post/2021-11-container-escape) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth case study of container escape tactics and real-time detection utilizing eBPF and Cilium. It highlights limits of traditional syscall auditing, showcasing how kernel-level hooks identify privilege escalation without agent-induced overhead. Live Grounding points to eBPF-based security as the modern baseline for runtime security orchestration.
### Secrets Management (2)

#### Conceptual (1)

  - **(2022)** [macchaffee.com: Plain Kubernetes Secrets are fine 🌟](https://www.macchaffee.com/blog/2022/k8s-secrets)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An alternative architectural perspective defending native Kubernetes Secrets. Argues that when matched with strong RBAC controls, namespace boundaries, and cluster-level etcd KMS encryption, native solutions provide sufficient enterprise protection.
  - **(2019)** [enterprisersproject.com: How to explain Kubernetes Secrets in plain English 🌟](https://enterprisersproject.com/article/2019/8/kubernetes-secrets-explained-plain-english)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory conceptual explanation of Kubernetes Secrets. Translates low-level pod definitions and etcd mappings into non-technical language to align business stakeholders on cloud-native security postures.
#### Developer Practice

  - **(2021)** [millionvisit.blogspot.com: Kubernetes for Developers #19: Manage app credentials using Kubernetes Secrets 🌟](http://millionvisit.blogspot.com/2021/07/kubernetes-for-developers-19-manage-app-credentials-using-Kubernetes-Secrets.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Developer-centric guide to configuring application manifests for secret consumption. Compares the security profiles of importing secrets as environment variables against dynamic filesystem mounts, detailing runtime behavior and update propagation.
#### External Secrets

  - **(2025)** [==external-secrets.io 🌟==](https://external-secrets.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry-standard operator for syncing external secrets management services (like AWS Secrets Manager, Vault, or GCP Secret Manager) into Kubernetes Secret objects. This eliminates storing sensitive configuration inside git repositories, supporting true GitOps workflows. Decoupled and secure, it is a critical security-centric component.
#### GitOps

##### External Secrets Operator

  - **(2023)** [youtube: Manage Kubernetes Secrets With External Secrets Operator (ESO) 🌟](https://www.youtube.com/watch?v=SyRZe5YVCVk)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A technical demonstration detailing the installation and runtime management of the External Secrets Operator (ESO). Demonstrates synchronization pipelines that pull credentials from HashiCorp Vault and cloud providers into native secret schemas.
##### Sealed Secrets

  - **(2022)** [dev.to: Store your Kubernetes Secrets in Git thanks to Kubeseal. Hello SealedSecret! 🌟](https://dev.to/stack-labs/store-your-kubernetes-secrets-in-git-thanks-to-kubeseal-hello-sealedsecret-2i6h)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A step-by-step implementation guide for Bitnami's Sealed Secrets (kubeseal). Explains how asymmetric cryptography allows developers to safely commit encrypted secrets to public repositories, leaving cluster-side controllers to handle automated decryption.
  - **(2022)** [piotrminkowski.com: Sealed Secrets on Kubernetes with ArgoCD and Terraform](https://piotrminkowski.com/2022/12/14/sealed-secrets-on-kubernetes-with-argocd-and-terraform) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates the end-to-end automation of Bitnami Sealed Secrets using Terraform and ArgoCD. Helps DevOps architects define declarative pipelines that provision the sealed secret operator and manage encrypted configurations in Git repositories.
  - **(2022)** [cloud.redhat.com: A Guide to Secrets Management with GitOps and Kubernetes 🌟](https://www.redhat.com/en/blog/a-guide-to-secrets-management-with-gitops-and-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's whitepaper outlining standard solutions for GitOps secrets management. Contrasts the operational overhead and security profiles of Sealed Secrets, vault-sidecars, and external integration engines in CD environments.
#### HashiCorp Vault

  - **(2021)** [itnext.io: Effective Secrets with Vault and Kubernetes](https://itnext.io/effective-secrets-with-vault-and-kubernetes-9af5f5c04d06) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural overview on configuring HashiCorp Vault inside Kubernetes clusters. Covers the Vault Agent Sidecar Injector pattern, dynamic database credential generation, and leveraging Kubernetes service accounts for seamless Vault token exchange.
  - **(2021)** [itnext.io: Vault cluster with auto unseal on Kubernetes](https://itnext.io/vault-cluster-with-auto-unseal-on-kubernetes-8e469f9cdcfd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed structural guide for configuring an enterprise-grade, highly available HashiCorp Vault cluster in Kubernetes. Features automated unsealing integrations using cloud KMS systems (AWS KMS/GCP KMS) to remove manual keys dependencies.
#### KMS Integration

##### Legacy Tools (4)

  - **(2023)** [==github.com/ondat/trousseau==](https://github.com/ondat/trousseau) <span class='md-tag md-tag--info'>⭐ 181</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight: KMS integration designed to encrypt secrets inside etcd using external key management systems. Live Grounding: This repository is unmaintained and archived following Ondat's acquisition. Deprioritized under MVQ rules in favor of native Kubernetes KMS v2 features.
#### OWASP

  - **(2022)** [itnext.io: Kubernetes OWASP Top 10: Secrets Management](https://itnext.io/kubernetes-owasp-top-10-secrets-management-c996faa87b47)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Addresses Secrets Management under the OWASP Kubernetes threat framework. Details vulnerabilities of default etcd storage parameters and details using External Secrets Operator or HashiCorp Vault. Prevents secrets exposure via repository check-ins or pod environment parameters.
#### Platform Hardening (1)

##### Conceptual (2)

  - **(2022)** ["Kubernetes base64 encodes secrets because that makes arbitrary data play nice with JSON. It had nothing to do with the security model (or lack thereof). It did not occur to us at the time that people could mistake base64 for some form of encryption"](https://x.com/originalavalamp)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated synthesis of engineering consensus regarding Kubernetes native base64 secrets. Emphasizes that encoding is not encryption and acts strictly as a data-serialization layer. Highly recommends implementing RBAC, audit logging, and envelope KMS encryption.
  - **(2026)** [kubernetes.io: Encrypting Secret Data at Rest 🌟](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official reference guide to implementing etcd database encryption at rest. Walks through configuring structural 'EncryptionConfiguration' resources, comparing local providers (AES-GCM, secretbox) against enterprise Cloud KMS plugins.
#### Stateful Apps

  - **(2021)** [kubermatic.com: Keeping the State of Apps Part 2: Introduction to Secrets](https://www.kubermatic.com/blog/keeping-the-state-of-apps-part-2-introduction-to-secrets)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An overview of state management strategies within modern Kubernetes runtimes. Highlights basic secrets integration patterns, emphasizing security isolation layers required to protect persistent state in complex application architectures.
### Static Analysis

#### Manifest Auditing (1)

  - **(2022)** [itnext.io: Performing Security Checks for Deployed Kubernetes Manifests](https://itnext.io/performing-security-checks-for-deployed-kubernetes-manifests-fa9d442b7951)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews technical methods to assess security profiles of Kubernetes configurations prior to cluster deployment. Explains standard static evaluation tools and custom policy syntax like Open Policy Agent (OPA) or Kyverno. Focuses on integrating these guardrails directly within pull request pipelines.
### System Hardening

#### Security Profiles Operator

  - **(2025)** [**kubernetes-sigs/security-profiles-operator**](https://github.com/kubernetes-sigs/security-profiles-operator) <span class='md-tag md-tag--info'>⭐ 848</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official Kubernetes SIG operator for managing Seccomp, AppArmor, and SELinux profiles natively. Live Grounding confirms its active role in highly regulated sectors for hardening container execution spaces. It replaces manual node profiling with declarative, cluster-wide configurations.
  - **(2021)** [kubernetes.io: What's new in Security Profiles Operator v0.4.0](https://kubernetes.io/blog/2021/12/17/security-profiles-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official release announcement detailing the evolution of SPO. It highlights improved profile recording capabilities, integration with kubectl, and initial support for SELinux. Crucial for understanding the transition from manual profiles to automation.
### Threat Modeling (1)

#### Penetration Testing (2)

  - **(2021)** [dev.to: A Detailed Talk about K8S Cluster Security from the Perspective of Attackers (Part 1)](https://dev.to/tutorialboy/a-detailed-talk-about-k8s-cluster-security-from-the-perspective-of-attackers-part-1-3mm5) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides an attacker's perspective on Kubernetes deployment flaws. Explores breakout methodologies, privilege escalation via over-permissioned service accounts, and API Server compromise scenarios, illustrating defensive configurations required to counter threats.
### Threat Vector

#### Internet Exposure (1)

  - **(2023)** [blog.cyble.com: Exposed Kubernetes Clusters](https://cyble.com/blog/exposed-kubernetes-clusters) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Threat intelligence research showing search profiles of exposed clusters active across the globe. Highlights typical compromise pathways starting from default configurations or misconfigured control plane boundaries. Recommends strict perimeter restrictions.
#### Observability Exposure

  - **(2022)** [sysdig.com: How attackers use exposed Prometheus server to exploit Kubernetes clusters | Miguel Hernández](https://www.sysdig.com/blog/exposed-prometheus-exploit-kubernetes-kubeconeu) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical threat report detailing how exposed Prometheus endpoints can facilitate cluster compromise. Explains how attackers scan for unauthenticated metrics interfaces to harvest metadata, endpoints, and environment configurations. Demonstrates step-by-step mitigation paths, including mandatory mTLS and RBAC verification.
### Tooling

#### Security Auditing (1)

  - **(2022)** [mattermost.com: The Top 7 Open Source Tools for Securing Your Kubernetes Cluster](https://mattermost.com/blog/the-top-7-open-source-tools-for-securing-your-kubernetes-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This resource provides a comparative overview of seven premier open-source tools designed for Kubernetes security hardening. It introduces utilities like Trivy, Falco, and Kube-hunter, aligning each with specific pipeline gates or runtime defenses. Serves as a useful high-level map for architects selecting security tooling.
### Vulnerabilities

#### CVE Tracking

  - **(2025)** [kubernetes.io: Official CVE Feed 🌟](https://kubernetes.io/docs/reference/issues-security/official-cve-feed) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official database of active and resolved CVEs for the Kubernetes ecosystem. It tracks core component bugs, container execution vulnerabilities, and control plane bypass vectors. Maintaining a regular review of this feed is an essential component of modern enterprise risk mitigation.
  - **(2022)** [kubernetes.io: Announcing the Auto-refreshing Official Kubernetes CVE Feed](https://kubernetes.io/blog/2022/09/12/k8s-cve-feed-alpha)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the launch of the programmatically accessible, auto-refreshing CVE feed in JSON/YAML. This allows security automation tooling to dynamically scan and trigger alerts on freshly discovered platform vulnerabilities, greatly speeding up remediation and patching schedules.
#### Case Studies (1)

  - **(2021)** [hackerone.com: Authenticated kubernetes principal with restricted permissions can retrieve ingress-nginx serviceaccount token and secrets across all namespaces](https://hackerone.com/reports/1249583) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed post-mortem report demonstrating how restricted cluster principals could extract ingress-nginx service account tokens. This real-world vulnerability highlights the architectural danger of over-privileged system namespaces. It emphasizes the need to isolate and continuously audit ingress controller configurations.
#### Post-Deployment Scanning

  - **(2025)** [==kubescape==](https://github.com/kubescape/kubescape) <span class='md-tag md-tag--info'>⭐ 11480</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An active CNCF Sandbox tool providing multi-framework configuration scanning, risk analysis, and vulnerability management. It integrates into CI/CD pipelines to ensure continuous verification of compliance frameworks (like CIS and NSA-CISA). Essential for enterprise teams seeking unified security visibility.
### Vulnerability Assessment

#### CIS Benchmarks (1)

  - **(2022)** [rancher/cis-operator](https://github.com/rancher/cis-operator) <span class='md-tag md-tag--info'>⭐ 55</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Rancher's cis-operator is an automated tool running CIS security scans natively within Rancher ecosystems. It generates compliance reports validating control plane and worker components against standard security baselines. A key utility for multi-cluster environments managed via Rancher.
  - **(2022)** [blog.flant.com: Kubernetes cluster security assessment with kube-bench and kube-hunter](https://palark.com/blog/kubernetes-security-with-kube-bench-and-kube-hunter)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates how to deploy and configure Aqua Security's kube-bench alongside kube-hunter. Shows how to automate node validation against CIS benchmarks, and actively scan cluster endpoints for network exposure vectors. Offers a potent open-source combination for regular pentesting operations.
#### Policy Enforcement (1)

  - **(2023)** [**github.com/Shopify/kubeaudit 🌟🌟**](https://github.com/Shopify/kubeaudit) <span class='md-tag md-tag--info'>⭐ 1937</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Shopify's kubeaudit is a popular open-source tool targeting configuration analysis. Curators note its ability to audit running clusters or local manifests for root execution or privilege escalations. *Live Grounding (2026)*: The repository is archived/read-only, but its audit logic remains highly influential for policy structures.
  - **(2022)** [itnext.io: Kubernetes OWASP Top 10: Centralised Policy Enforcement](https://itnext.io/kubernetes-owasp-top-10-centralised-policy-enforcement-9adc53438e22)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates mitigating risks from the OWASP Kubernetes Top 10 using centralized Policy-as-Code platforms like OPA Gatekeeper or Kyverno. Focuses on setting up mutating and validating admission webhooks to prevent non-compliant configs from deploying. Establishes programmatic posture control.
  - **(2021)** [infoq.com: Armo Releases Kubescape K8s Security Testing Tool: Q&A with VP Jonathan Kaftzan](https://www.infoq.com/news/2021/09/kubescape)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An interview exploring the architecture, technical goals, and philosophy behind Kubescape. Focuses on simplifying multi-framework compliance analysis for platform engineers. Details how the tool analyzes YAML formats and active runtimes to find security posture anomalies.
#### Threat Modeling (2)

  - **(2022)** [owasp.org: OWASP Kubernetes Top Ten](https://owasp.org/www-project-kubernetes-top-ten) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official OWASP Kubernetes Top Ten project document. Outlines the ten most dangerous vulnerabilities facing modern orchestrator deployments, including API vulnerabilities, insecure defaults, and supply-chain bugs. The core benchmark for establishing cluster defense strategies.
  - **(2022)** [sysdig.com: OWASP Kubernetes Top 10 🌟](https://www.sysdig.com/blog/top-owasp-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep analysis of the OWASP Kubernetes Top 10, exploring actual deployment misconfigurations that map to these risks. Details supply chain threats, poor credentials storage, and audit log gaps. Offers recommendations to strengthen system setups.
### Zero Trust

#### Service Mesh and Networking

  - **(2022)** [copado.com: Applying a Zero Trust Infrastructure in Kubernetes](https://www.copado.com/resources/blog/applying-a-zero-trust-infrastructure-in-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architecture guide on applying Zero Trust principles to Kubernetes infrastructure environments. It covers building cryptographically verifiable workload identities via SPIFFE/SPIRE, and micro-segmenting service interactions with mTLS. Transitions teams away from perimeter-only defenses to continuous validation.
### Zero Trust Architecture

  - **(2022)** [thenewstack.io: Securing Access to Kubernetes Environments with Zero Trust](https://thenewstack.io/securing-access-to-kubernetes-environments-with-zero-trust)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses securing cloud-native setups using Zero Trust strategies. Covers real-time threat assessments, deep access auditing, and replacing static certificates with automated network micro-segmentation.
## Security Training and Playgrounds

### Kubernetes Goat Lab

  - **(2020)** [Kubernetes Goat 🌟](https://madhuakula.com/kubernetes-goat) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An intentionally vulnerable cluster environment designed for hands-on cybersecurity training. Includes self-contained scenarios exploring SSRF, container escape, secrets leakage, and misconfigured RBAC roles.
## Supply Chain Security

### Open Source Vulnerability Scanning

  - **(2020)** [resources.whitesourcesoftware.com: Kubernetes Security Best Practices 🌟](https://resources.whitesourcesoftware.com/blog-whitesource/kubernetes-security) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details patterns for implementing automated security controls, concentrating on software composition analysis (SCA), secrets lifecycle management, and validating supply-chain container provenance.
### Signature Verification and Ratify

  - **(2021)** [infoworld.com: Securing the Kubernetes software supply chain with Microsoft's Ratify](https://www.infoworld.com/article/2271333/securing-the-kubernetes-software-supply-chain.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on utilizing Ratify as an admission controller to verify container metadata, secure supply-chain signatures (via Cosign/Notation), and enforce strict provenance validation before execution.
## Threat Modeling (3)

### MITRE ATTandCK Adaptation

  - **(2021)** [microsoft.com: Secure containerized environments with updated threat matrix for Kubernetes](https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses updates to Microsoft's threat matrix for Kubernetes, refining mapped attack vectors based on modern production compromise telemetry. Covers control plane compromises and cloud identity integrations.
### MITRE ATTandCK Framework

  - **(2020)** [Microsoft.com: Attack matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Microsoft's systematic adaptation of the MITRE ATT&CK framework mapping out K8s attack vectors from initial access to execution, persistence, privilege escalation, and impact. Helps security operators assess risks in orchestration configurations.
## Vulnerability Assessment Tools

### Kubestriker Scanner

  - **(2021)** [helpnetsecurity.com: Kubestriker: A security auditing tool for Kubernetes clusters 🌟](https://www.helpnetsecurity.com/2021/05/04/security-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews Kubestriker, a lightweight, agentless open-source security scanner that audits Kubernetes control plane configurations, insecure ports, and IAM roles for vulnerabilities.
## Workload Hardening

### Identity and Access Management (2)

  - **(2020)** [thenewstack.io: Laying the Groundwork for Kubernetes Security, Across Workloads, Pods and Users](https://thenewstack.io/laying-the-groundwork-for-kubernetes-security-across-workloads-pods-and-users) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the multi-dimensional security layers required for modern Kubernetes deployments, addressing workload isolation, Pod Security Standards (PSS), and secure developer workflow patterns.
### Pod Security Context

  - **(2020)** [snyk.io: 10 Kubernetes Security Context settings you should understand](https://snyk.io/blog/10-kubernetes-security-context-settings-you-should-understand) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed documentation of essential Security Context settings (e.g., `allowPrivilegeEscalation`, `readOnlyRootFilesystem`, and `runAsNonRoot`) used to harden workload runtimes.
### Pod Specifications

  - **(2021)** [blog.gitguardian.com: Kubernetes Hardening Tutorial Part 1: Pods](https://blog.gitguardian.com/kubernetes-tutorial-part-1-pods) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of GitGuardian's workload security tutorial, targeting critical pod configurations such as root user restrictions, secure namespaces, and minimizing host-level network sharing.
## Workstation Client Security

### Kubeconfig Hardening

  - **(2020)** [gist.github.com: How to protect your ~/.kube/ configuration](https://gist.github.com/PatrLind/e651d3cbc3bf68e4bd9fcc9568cbd3fb) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides hardening steps for securing developer workstation `~/.kube/config` files. Details POSIX permissions adjustments, the usage of credential helpers, and avoiding static administrative token storage.

---
💡 **Explore Related:** [IaC](./iac.md) | [Terraform](./terraform.md) | [Oauth](./oauth.md)

