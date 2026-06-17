# Managed Kubernetes in Public Cloud

!!! info "Architectural Context"
    Detailed reference for Managed Kubernetes in Public Cloud in the context of Cloud Providers (Hyperscalers).

## Alternative Cloud

### DigitalOcean Kubernetes DOKS

#### Core Platforms

  - **(2025)** [docs.digitalocean.com: Kubernetes on DigitalOcean](https://docs.digitalocean.com/products/kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The baseline documentation hub for DigitalOcean Kubernetes (DOKS). Features developer-friendly setup guides, automated node pool configurations, and block storage integrations. Recommended for startups and medium-sized application workloads seeking an intuitive managed container orchestrator.
#### GitOps and Continuous Delivery

  - **(2022)** [digitalocean.com: Automating GitOps and Continuous Delivery With DigitalOcean Kubernetes (Terraform, Helm and Flux)](https://www.digitalocean.com/community/tech-talks/automating-gitops-and-continuous-delivery-with-digitalocean-kubernetes) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide on implementing declarative GitOps structures on DOKS using Flux CD, Terraform, and Helm charts. Provides a complete architectural template for managing infrastructure and application configurations declaration-first, reducing configuration drift in production.
### IBM Kubernetes Service IKS

#### Core Platforms (1)

  - **(2025)** [IKS](https://www.ibm.com/products/kubernetes-service) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official landing documentation for IBM Cloud Kubernetes Service (IKS). Highlights its integration with IBM's compliance profiles, hardware security modules (HSM), and bare-metal nodes. A useful reference for enterprise cloud-native architects looking for secure hybrid options.
### Linode Kubernetes Engine LKE

#### Autoscaling Core

  - **(2022)** [dev.to: Practical Introduction to Kubernetes Autoscaling Tools with Linode Kubernetes Engine 🌟](https://dev.to/rahulrai/practical-introduction-to-kubernetes-autoscaling-tools-with-linode-kubernetes-engine-2i7k) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to Kubernetes scaling tools (HPA, VPA, and Cluster Autoscaler) leveraging the Linode Kubernetes Engine (LKE). This guide demystifies metric validation loops and autoscaler behavior, providing a practical foundation for engineers implementing scaling outside major hyperscalers.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [medium.com/@ishana98dadhich: Integrating AWS Secret Manager with EKS and' use Secrets inside the Pods: Part-1](https://medium.com/@ishana98dadhich/integrating-aws-secret-manager-with-eks-and-use-secrets-inside-the-pods-part-1-1938b0c3c2fb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@ishana98dadhich: Integrating AWS Secret Manager with EKS and' use Secrets inside the Pods: Part-1 in the Kubernetes Tools ecosystem.
  - [mehighlow.medium.com: Hardened-AKS/Secrets](https://mehighlow.medium.com/hardened-aks-secrets-82351c43eac4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==mehighlow.medium.com: Hardened-AKS/Secrets== in the Kubernetes Tools ecosystem.
  - [medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS](https://medium.com/@Platform9Sys/kubernetes-cloud-services-comparing-gke-eks-and-aks-1fe42770cad3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com: Kubernetes Cloud Services: Comparing GKE, EKS and AKS in the Kubernetes Tools ecosystem.
  - [medium: State of Managed Kubernetes 2020](https://medium.com/swlh/state-of-managed-kubernetes-2020-4be006643360)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: State of Managed Kubernetes 2020 in the Kubernetes Tools ecosystem.
  - [medium: Managed Kubernetes Services Compared: GKE vs. EKS vs. AKS](https://medium.com/better-programming/managed-kubernetes-services-compared-gke-vs-eks-vs-aks-df1ecb22bba0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Managed Kubernetes Services Compared: GKE vs. EKS vs. AKS in the Kubernetes Tools ecosystem.
  - [otomi.io 🌟](https://otomi.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering otomi.io 🌟 in the Kubernetes Tools ecosystem.
  - [udemy.com: amazon eks starter kubernetes on aws](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering udemy.com: amazon eks starter kubernetes on aws in the Kubernetes Tools ecosystem.
  - [magalix.com: Deploying Kubernetes Cluster With EKS 🌟](https://www.magalix.com/blog/deploying-kubernetes-cluster-with-eks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering magalix.com: Deploying Kubernetes Cluster With EKS 🌟 in the Kubernetes Tools ecosystem.
  - [Deploying Infrastructure (FrontEnd + BackEnd) on AWS using Amazon EKS](https://medium.com/@ghumare64/deploying-infrastructure-frontend-backend-on-aws-using-amazon-eks-5f1f426d618e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Deploying Infrastructure (FrontEnd + BackEnd) on AWS using Amazon EKS in the Kubernetes Tools ecosystem.
  - [medium: Building the CI/CD of the Future, Creating the EKS Cluster 🌟](https://medium.com/swlh/building-the-ci-cd-of-the-future-creating-the-eks-cluster-e4cce4eb3500)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Building the CI/CD of the Future, Creating the EKS Cluster 🌟 in the Kubernetes Tools ecosystem.
  - [daveops.xyz: Administrar usuarios en EKS](https://daveops.xyz/2020/08/25/administrar-usuarios-en-eks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering daveops.xyz: Administrar usuarios en EKS in the Kubernetes Tools ecosystem.
  - [medium: Designing a Kubernetes Cluster with Amazon EKS From Scratch 🌟](https://medium.com/adobetech/designing-a-kubernetes-cluster-with-amazon-eks-from-scratch-4b4ee9d1b8f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Designing a Kubernetes Cluster with Amazon EKS From Scratch 🌟 in the Kubernetes Tools ecosystem.
  - [en.sokube.ch: AWS + Kubernetes = AWS Elastic Kubernetes Service (EKS) 🌟](https://en.sokube.ch/post/aws-kubernetes-aws-elastic-kubernetes-service-eks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering en.sokube.ch: AWS + Kubernetes = AWS Elastic Kubernetes Service (EKS) 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Run Kubernetes Production Environment on EC2 Spot Instances With' Zero Downtime: A Complete Guide](https://medium.com/riskified-technology/run-kubernetes-on-aws-ec2-spot-instances-with-zero-downtime-f7327a95dea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Run Kubernetes Production Environment on EC2 Spot Instances With' Zero Downtime: A Complete Guide in the Kubernetes Tools ecosystem.
  - [releaseops.io: Scaling Kubernetes Deployments in AWS with Container Insights' Metrics](https://releaseops.io/blog/scaling-kubernetes-deployments-in-aws-with-container-insights-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering releaseops.io: Scaling Kubernetes Deployments in AWS with Container Insights' Metrics in the Kubernetes Tools ecosystem.
  - [medium: Create Kubernetes Cluster On AWS EKS](https://medium.com/codex/create-kubernetes-cluster-on-aws-eks-6ced4c488e62)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Create Kubernetes Cluster On AWS EKS in the Kubernetes Tools ecosystem.
  - [info.acloud.guru: Scaling the hottest app in tech on AWS and Kubernetes](https://info.acloud.guru/resources/kubernetes-aws-cloud-scaling-hey)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering info.acloud.guru: Scaling the hottest app in tech on AWS and Kubernetes in the Kubernetes Tools ecosystem.
  - [medium: How to Deploy an EKS stack in AWS?](https://medium.com/avmconsulting-blog/how-to-deploy-an-eks-stack-to-kubernetes-aws-5ec9c5a07247)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: How to Deploy an EKS stack in AWS? in the Kubernetes Tools ecosystem.
  - [faun.pub: Upgrading and Scaling Kubernetes cluster in AWS](https://faun.pub/upgrading-and-scaling-kubernetes-cluster-in-aws-6971b3936465)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Upgrading and Scaling Kubernetes cluster in AWS in the Kubernetes Tools ecosystem.
  - [particule.io: Create Kubernetes federated clusters on AWS](https://particule.io/en/blog/aws-federated-eks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering particule.io: Create Kubernetes federated clusters on AWS in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Amazon EKS Is Eating My IPs!](https://betterprogramming.pub/amazon-eks-is-eating-my-ips-e18ea057e045)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Amazon EKS Is Eating My IPs! in the Kubernetes Tools ecosystem.
  - [blog.usejournal.com: Spice up Your Kubernetes Environment with AWS Lambda' 🌟](https://blog.usejournal.com/spice-up-your-kubernetes-environment-with-aws-lambda-a07d81347607)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.usejournal.com: Spice up Your Kubernetes Environment with AWS Lambda' 🌟 in the Kubernetes Tools ecosystem.
  - [neal-davis.medium.com: ECS vs EC2 vs Lambda](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering neal-davis.medium.com: ECS vs EC2 vs Lambda in the Kubernetes Tools ecosystem.
  - [faun.pub: Kubernetes Multi-tenancy with Amazon EKS: Best practices and considerations' 🌟](https://faun.pub/kubernetes-multi-tenancy-with-amazon-eks-best-practices-and-considerations-60bfd78c2f9a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Kubernetes Multi-tenancy with Amazon EKS: Best practices and considerations' 🌟 in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: 6 Tips to Improve Availability with AWS Load Balancers' and Kubernetes](https://aws.plainenglish.io/6-tips-to-improve-availability-with-aws-load-balancers-and-kubernetes-ad8d4d1c0f61)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: 6 Tips to Improve Availability with AWS Load Balancers' and Kubernetes in the Kubernetes Tools ecosystem.
  - [blog.searce.com: Optimise cost for AWS EKS cluster using Spotinst 🌟](https://blog.searce.com/optimize-cost-for-aws-eks-cluster-using-spotinst-ffcebe8e3571)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.searce.com: Optimise cost for AWS EKS cluster using Spotinst 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@abhinav.ittekot: Granting IAM permissions to pods in EKS using' OIDC](https://medium.com/@abhinav.ittekot/granting-iam-permissions-to-pods-in-eks-using-oidc-f2044c88a53)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@abhinav.ittekot: Granting IAM permissions to pods in EKS using' OIDC in the Kubernetes Tools ecosystem.
  - [medium.com/@radha.sable25: Enabling IAM users/roles Access on Amazon EKS' cluster](https://medium.com/@radha.sable25/enabling-iam-users-roles-access-on-amazon-eks-cluster-f69b485c674f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@radha.sable25: Enabling IAM users/roles Access on Amazon EKS' cluster in the Kubernetes Tools ecosystem.
  - [medium.com/avmconsulting-blog: Installing Vault On EKS With TLS And Persistent' Storage](https://medium.com/avmconsulting-blog/installing-vault-on-eks-with-tls-and-persistent-storage-98254b4150f3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/avmconsulting-blog: Installing Vault On EKS With TLS And Persistent' Storage in the Kubernetes Tools ecosystem.
  - [dzone.com: How to Use AWS IAM Role on AWS EKS PODs 🌟](https://dzone.com/articles/how-to-use-aws-iam-role-on-aws-eks-pods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone.com: How to Use AWS IAM Role on AWS EKS PODs 🌟 in the Kubernetes Tools ecosystem.
  - [akintola-lonlon.medium.com: AWS Kubernetes: The #1 Rule You Need To Master' Before Going To Production.](https://akintola-lonlon.medium.com/aws-kubernetes-the-1-rule-you-need-to-master-before-going-to-production-628b75ba1b6a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering akintola-lonlon.medium.com: AWS Kubernetes: The #1 Rule You Need To Master' Before Going To Production. in the Kubernetes Tools ecosystem.
  - [amod-kadam.medium.com: Are there two Load Balancer Controllers with EKS?' 🌟](https://amod-kadam.medium.com/are-there-two-load-balancer-controllers-with-eks-8a7b04db8c93)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering amod-kadam.medium.com: Are there two Load Balancer Controllers with EKS?' 🌟 in the Kubernetes Tools ecosystem.
  - [joachim8675309.medium.com: ExternalDNS with EKS and Route53](https://joachim8675309.medium.com/externaldns-with-eks-and-route53-90aa23fa3aba)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering joachim8675309.medium.com: ExternalDNS with EKS and Route53 in the Kubernetes Tools ecosystem.
  - [opssorry.substack.com: GitOps: A Simple Approach to using AWS Secrets' Manager with Kubernetes 🌟](https://opssorry.substack.com/p/gitops-a-simple-approach-to-using)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==opssorry.substack.com: GitOps: A Simple Approach to using AWS Secrets' Manager with Kubernetes== 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@chandranathmondal: Self-service Amazon EKS Cluster provisioning' with Kubernetes configuration applied 🌟](https://medium.com/@chandranathmondal/self-service-amazon-eks-cluster-provisioning-with-kubernetes-configuration-applied-372bce839d7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@chandranathmondal: ==Self-service Amazon EKS Cluster provisioning' with Kubernetes configuration applied== 🌟 in the Kubernetes Tools ecosystem.
  - [eng.grip.security: Enabling AWS IAM Group Access to an EKS Cluster Using' RBAC](https://eng.grip.security/enabling-aws-iam-group-access-to-an-eks-cluster-using-rbac)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering eng.grip.security: Enabling AWS IAM Group Access to an EKS Cluster Using' RBAC in the Kubernetes Tools ecosystem.
  - [medium.com/@andriikrymus: DNS config for EKS](https://medium.com/@andriikrymus/dns-config-for-eks-61eb70c3e31e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@andriikrymus: DNS config for EKS in the Kubernetes Tools ecosystem.
  - [silvr.medium.com: Using Kyverno To Enforce AWS Load Balancer Annotations' For Centralized Logging To S3](https://silvr.medium.com/using-kyverno-to-enforce-aws-load-balancer-annotations-for-centralized-logging-to-s3-af5dc1f1f3e0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering silvr.medium.com: Using Kyverno To Enforce AWS Load Balancer Annotations' For Centralized Logging To S3 in the Kubernetes Tools ecosystem.
  - [blog.jimmyray.io: Kubernetes Workload Identity with AWS SDK for Go v2](https://blog.jimmyray.io/kubernetes-workload-identity-with-aws-sdk-for-go-v2-927d2f258057)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.jimmyray.io: Kubernetes Workload Identity with AWS SDK for Go v2 in the Kubernetes Tools ecosystem.
  - [medium.com/geekculture: EKS — Kubernetes — Not Ready nodes](https://medium.com/geekculture/eks-kubernetes-not-ready-nodes-dafb300ed299)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/geekculture: EKS — Kubernetes — Not Ready nodes in the Kubernetes Tools ecosystem.
  - [faun.pub: How to access AWS services from EKS](https://faun.pub/how-to-access-aws-services-from-eks-ab5fa003a1b6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==faun.pub: How to access AWS services from EKS== in the Kubernetes Tools ecosystem.
  - [faun.pub: AWS EKS: The Ultimate Guide To Deploy AWS Load Balancer Controller' add-on](https://faun.pub/aws-eks-the-ultimate-guide-to-deploy-an-ingress-controller-on-kubernetes-5952cb27c067)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: AWS EKS: The Ultimate Guide To Deploy AWS Load Balancer Controller' add-on in the Kubernetes Tools ecosystem.
  - [medium.com/@ankit.wal: Understanding IAM roles for service accounts, IRSA,' on AWS EKS](https://medium.com/@ankit.wal/the-how-of-iam-roles-for-service-accounts-irsa-on-aws-eks-3d76badb8942)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/@ankit.wal: Understanding IAM roles for service accounts, IRSA,' on AWS EKS== in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: Running Workflows on windows with Jenkins pipeline' and Kubernetes](https://levelup.gitconnected.com/running-workflows-on-windows-with-jenkins-pipeline-and-kubernetes-52752a89a0e7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: Running Workflows on windows with Jenkins pipeline' and Kubernetes in the Kubernetes Tools ecosystem.
  - [nivogt.medium.com: Boost your Kubernetes cluster’s Autoscaler on AWS EKS' with Karpenter](https://nivogt.medium.com/boost-your-kubernetes-clusters-autoscaler-on-aws-eks-with-karpenter-4d23955944f2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering nivogt.medium.com: Boost your Kubernetes cluster’s Autoscaler on AWS EKS' with Karpenter in the Kubernetes Tools ecosystem.
  - [towardsaws.com: Autoscale Kubernetes Metrics Server on Amazon EKS](https://towardsaws.com/autoscale-kubernetes-metrics-server-fa398f8a600a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering towardsaws.com: Autoscale Kubernetes Metrics Server on Amazon EKS in the Kubernetes Tools ecosystem.
  - [faun.pub: Analyze AWS EKS Audit logs with Falco](https://faun.pub/analyze-aws-eks-audit-logs-with-falco-95202167f2e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Analyze AWS EKS Audit logs with Falco in the Kubernetes Tools ecosystem.
  - [hardiks.medium.com: Where should you manage your Kubernetes in 2023? Amazon' ECS or EKS](https://hardiks.medium.com/where-should-you-manage-your-kubernetes-in-2023-amazon-ecs-or-eks-6f503e93f7a7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering hardiks.medium.com: Where should you manage your Kubernetes in 2023? Amazon' ECS or EKS in the Kubernetes Tools ecosystem.
  - [awstip.com: Amazon Elastic Kubernetes Service (Amazon EKS) — The Only Resource' Hub You Ever Need](https://awstip.com/amazon-elastic-kubernetes-service-amazon-eks-the-only-resource-hub-you-ever-need-3b802687df36)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering awstip.com: Amazon Elastic Kubernetes Service (Amazon EKS) — The Only Resource' Hub You Ever Need in the Kubernetes Tools ecosystem.
  - [awstip.com: Working The Amazon EKS Immersion Workshop — Chapter 1 — Deploying' A Microservices Application In A Kubernetes Cluster](https://awstip.com/working-the-amazon-eks-immersion-workshop-chapter-1-deploying-a-microservices-application-in-a-9acae5df2f01)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering awstip.com: Working The Amazon EKS Immersion Workshop — Chapter 1 — Deploying' A Microservices Application In A Kubernetes Cluster in the Kubernetes Tools ecosystem.
  - [blog.antoinechoula.ga: Native EKS Ingress with AWS Load Balancer Controller](https://blog.antoinechoula.ga/native-eks-ingress-with-aws-load-balancer-controller)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.antoinechoula.ga: Native EKS Ingress with AWS Load Balancer Controller in the Kubernetes Tools ecosystem.
  - [devopslearning.medium.com: Lesson learned while scaling Kubernetes cluster' to 1000 pods in AWS EKS](https://devopslearning.medium.com/lesson-learned-while-scaling-kubernetes-cluster-to-1000-pods-in-aws-eks-d2d399152bc2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering devopslearning.medium.com: Lesson learned while scaling Kubernetes cluster' to 1000 pods in AWS EKS in the Kubernetes Tools ecosystem.
  - [sitepoint.com: Getting Started With Kubernetes on AWS Tutorial (2023 Update)](https://www.sitepoint.com/kubernetes-aws-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering sitepoint.com: Getting Started With Kubernetes on AWS Tutorial (2023 Update) in the Kubernetes Tools ecosystem.
  - [medium.com: Saving costs in Google Kubernetes Engine using Spot VMs](https://medium.com/@vaibhav176/saving-costs-in-google-kubernetes-engine-using-spot-vms-2e6d0157815e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com: Saving costs in Google Kubernetes Engine using Spot VMs in the Kubernetes Tools ecosystem.
  - [medium.com/@benjamin.christmann_12432: Setting up your first EKS cluster' on AWS: some practical tips](https://medium.com/@benjamin.christmann_12432/setting-up-your-first-eks-cluster-on-aws-some-practical-tips-60400963c588)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@benjamin.christmann_12432: Setting up your first EKS cluster' on AWS: some practical tips in the Kubernetes Tools ecosystem.
  - [blog.ratnopamc.com: Reduce cross-AZ traffic costs on EKS using topology' aware hints](https://blog.ratnopamc.com/reduce-cross-az-traffic-costs-on-eks-using-topology-aware-hints)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.ratnopamc.com: Reduce cross-AZ traffic costs on EKS using topology' aware hints in the Kubernetes Tools ecosystem.
  - [medium.com/@danielresponda: Testing Spot Reclamation Mechanisms with AWS' Node Termination Handler and Kubernetes Autoscaler](https://medium.com/@danielresponda/testing-spot-reclamation-mechanisms-with-aws-node-termination-handler-and-kubernetes-autoscaler-43194d05dae0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@danielresponda: Testing Spot Reclamation Mechanisms with AWS' Node Termination Handler and Kubernetes Autoscaler in the Kubernetes Tools ecosystem.
  - [medium.com/@leocherian: Simple CDK app to create EKS Cluster](https://medium.com/@leocherian/simple-cdk-app-to-create-eks-cluster-06f651a12ccd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@leocherian: Simple CDK app to create EKS Cluster in the Kubernetes Tools ecosystem.
  - [blog.clouddrove.com: AWS EKS Blue/Green Deployment with Best Practices](https://blog.clouddrove.com/aws-eks-blue-green-deployment-with-best-practices-99be4b7baa38)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.clouddrove.com: AWS EKS Blue/Green Deployment with Best Practices in the Kubernetes Tools ecosystem.
  - [blog.stackademic.com: Create the AWS EKS Cluster with a Managed Node Group' Using Custom Launch Templates](https://blog.stackademic.com/create-the-aws-eks-cluster-with-a-managed-node-group-using-custom-launch-templates-185744a0cc79)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.stackademic.com: Create the AWS EKS Cluster with a Managed Node Group' Using Custom Launch Templates in the Kubernetes Tools ecosystem.
  - [blog.devops.dev: HACKING KUBERNETES in AWS](https://blog.devops.dev/hacking-kubernetes-in-aws-54f4681f1478)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.devops.dev: HACKING KUBERNETES in AWS in the Kubernetes Tools ecosystem.
  - [rahulbhatia1998.medium.com: Designing A Multi-Region Kubernetes Cluster' For Disaster Recovery On AWS EKS](https://rahulbhatia1998.medium.com/designing-a-multi-region-kubernetes-cluster-for-disaster-recovery-on-aws-eks-0a0a98ad5854)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering rahulbhatia1998.medium.com: Designing A Multi-Region Kubernetes Cluster' For Disaster Recovery On AWS EKS in the Kubernetes Tools ecosystem.
  - [towardsaws.com: From Scratch to Production: Deploying EKS Clusters and Applications' with CI/CD using Jenkins and Terraform](https://towardsaws.com/from-scratch-to-production-deploying-eks-clusters-and-applications-with-ci-cd-using-jenkins-and-f27d4686d5fe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering towardsaws.com: From Scratch to Production: Deploying EKS Clusters and Applications' with CI/CD using Jenkins and Terraform in the Kubernetes Tools ecosystem.
  - [awstip.com: Per-pod PIDs limit on EKS](https://awstip.com/per-pod-pids-limit-on-eks-fe320638c7e9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering awstip.com: Per-pod PIDs limit on EKS in the Kubernetes Tools ecosystem.
  - [medium.com/ekino-france: Addressing private IPv4 shortage: 5 Strategies' for Amazon EKS](https://medium.com/ekino-france/kubernetes-addressing-private-ipv4-shortage-5-strategies-for-amazon-eks-1dc3df270ed8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/ekino-france: Addressing private IPv4 shortage: 5 Strategies' for Amazon EKS in the Kubernetes Tools ecosystem.
  - [medium.com/scout24-engineering: How did we upgrade our EKS clusters from' 1.15 to 1.22 without K8s knowledge?](https://medium.com/scout24-engineering/how-did-we-upgrade-our-eks-clusters-from-1-15-to-1-22-without-k8s-knowledge-2c96c1a94cc1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/scout24-engineering: How did we upgrade our EKS clusters from' 1.15 to 1.22 without K8s knowledge? in the Kubernetes Tools ecosystem.
  - [marcincuber.medium.com: Amazon EKS Upgrade Journey From 1.24 to 1.25](https://marcincuber.medium.com/amazon-eks-upgrade-journey-from-1-24-to-1-25-e1bcccc2f384)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering marcincuber.medium.com: Amazon EKS Upgrade Journey From 1.24 to 1.25 in the Kubernetes Tools ecosystem.
  - [gokulchandrapr.medium.com: Amazon EKS Anywhere & EKS Connector](https://gokulchandrapr.medium.com/amazon-eks-anywhere-eks-connector-600953aaa42d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering gokulchandrapr.medium.com: Amazon EKS Anywhere & EKS Connector in the Kubernetes Tools ecosystem.
  - [ambar-thecloudgarage.medium.com: EKS Anywhere., decoding the architecture.](https://ambar-thecloudgarage.medium.com/eks-anywhere-decoding-the-architecture-fd2741b03e0a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ambar-thecloudgarage.medium.com: EKS Anywhere., decoding the architecture. in the Kubernetes Tools ecosystem.
  - [blog.techknowtrendz.com: Taking Amazon EKS Anywhere for a spin](https://blog.techknowtrendz.com/taking-amazon-eks-anywhere-for-a-spin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.techknowtrendz.com: Taking Amazon EKS Anywhere for a spin in the Kubernetes Tools ecosystem.
  - [medium: Kubernetes + EKS + Canary Deployment](https://medium.com/@jerome.decoster/kubernetes-eks-canary-deployment-1ef79ae89dfc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Kubernetes + EKS + Canary Deployment in the Kubernetes Tools ecosystem.
  - [mehmetozkaya.medium.com: Deploying .Net Microservices to Azure Kubernetes' Services(AKS) and Automating with Azure DevOps](https://mehmetozkaya.medium.com/deploying-net-microservices-to-azure-kubernetes-services-aks-and-automating-with-azure-devops-c50bdd51b702)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering mehmetozkaya.medium.com: Deploying .Net Microservices to Azure Kubernetes' Services(AKS) and Automating with Azure DevOps in the Kubernetes Tools ecosystem.
  - [faun.pub: How to implement Azure Kubernetes Service (AKS) in Cloud?](https://faun.pub/azure-kubernetes-service-aks-d1e71c7ecbe6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: How to implement Azure Kubernetes Service (AKS) in Cloud? in the Kubernetes Tools ecosystem.
  - [joachim8675309.medium.com: AKS with GRPC and ingress-nginx](https://joachim8675309.medium.com/aks-with-grpc-and-ingress-nginx-32481a792a1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering joachim8675309.medium.com: AKS with GRPC and ingress-nginx in the Kubernetes Tools ecosystem.
  - [medium: AKS with Calico Network Policies](https://medium.com/geekculture/aks-with-calico-network-policies-8cdfa996e6bb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: AKS with Calico Network Policies in the Kubernetes Tools ecosystem.
  - [joachim8675309.medium.com: AKS with Istio Service Mesh](https://joachim8675309.medium.com/istio-service-mesh-on-aks-1b6ed16f6890)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering joachim8675309.medium.com: AKS with Istio Service Mesh in the Kubernetes Tools ecosystem.
  - [blog.kasten.io: AKS and Storage: How to Design Storage for Cloud Native' Applications](https://blog.kasten.io/aks-and-storage-how-to-design-storage-for-cloud-native-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.kasten.io: AKS and Storage: How to Design Storage for Cloud Native' Applications in the Kubernetes Tools ecosystem.
  - [blog.kasten.io: AKS and Storage: Performance Differences Among K8s Storage' Services](https://blog.kasten.io/aks-and-storage-performance-differences-among-kubernetes-storage-services)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.kasten.io: AKS and Storage: Performance Differences Among K8s Storage' Services in the Kubernetes Tools ecosystem.
  - [medium: AKS — different load balancing options. When to use what?](https://medium.com/microsoftazure/aks-different-load-balancing-options-for-a-single-cluster-when-to-use-what-abd2c22c2825)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: AKS — different load balancing options. When to use what? in the Kubernetes Tools ecosystem.
  - [medium: Going multicloud with kubernetes and Azure Front Door](https://medium.com/microsoftazure/going-multicloud-with-kubernetes-and-azure-front-door-f34a2f39068a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Going multicloud with kubernetes and Azure Front Door in the Kubernetes Tools ecosystem.
  - [akhilsharma.work: How to list Azure RBAC Roles to Secure AKS Clusters](https://akhilsharma.work/how-to-list-azure-rbac-roles-to-secure-aks-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering akhilsharma.work: How to list Azure RBAC Roles to Secure AKS Clusters in the Kubernetes Tools ecosystem.
  - [logz.io: Collecting Metrics from Windows Kubernetes Nodes in AKS 🌟](https://logz.io/blog/windows-kubernetes-nodes-aks-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering logz.io: Collecting Metrics from Windows Kubernetes Nodes in AKS 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/kocsistem: Installation Internal Nginx Ingress for a Private' AKS Cluster](https://medium.com/kocsistem/installation-internal-nginx-ingress-for-a-private-aks-cluster-7b6386492d56)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/kocsistem: Installation Internal Nginx Ingress for a Private' AKS Cluster in the Kubernetes Tools ecosystem.
  - [joachim8675309.medium.com: ExternalDNS with AKS & Azure DNS](https://joachim8675309.medium.com/externaldns-with-aks-azure-dns-941a1804dc88)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering joachim8675309.medium.com: ExternalDNS with AKS & Azure DNS in the Kubernetes Tools ecosystem.
  - [medium.com/dzerolabs: Accessing Azure Key Vault Secrets in Azure Kubernetes' with Secrets Store CSI Driver 🌟](https://medium.com/dzerolabs/kubernetes-saved-today-f-cked-tomorrow-a-rant-azure-key-vault-secrets-%C3%A0-la-kubernetes-fc3be5e65d18)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/dzerolabs: Accessing Azure Key Vault Secrets in Azure Kubernetes' with Secrets Store CSI Driver 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@gjoshevski: Reduce the cost of running AKS cluster by leveraging' Azure Spot VMs| 70% and more 🌟🌟](https://medium.com/@gjoshevski/reduce-the-cost-of-running-aks-cluster-by-leveraging-azure-spot-vms-70-and-more-e917f568c3b9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/@gjoshevski: Reduce the cost of running AKS cluster by leveraging' Azure Spot VMs| 70% and more== 🌟🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/credera-engineering: How to blue-green deploy an AKS cluster](https://medium.com/credera-engineering/how-to-blue-green-deploy-an-aks-cluster-ab8f6a2cea9a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/credera-engineering: How to blue-green deploy an AKS cluster== in the Kubernetes Tools ecosystem.
  - [medium.com/@danieljimgarcia: The Application Gateway Ingress Controller' is broken 🌟](https://medium.com/@danieljimgarcia/the-application-gateway-ingress-controller-is-broken-6aa9eb229881)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/@danieljimgarcia: The Application Gateway Ingress Controller' is broken== 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@ershivamgupta: Disaster Recovery Solution for Azure Kubernetes' Service (AKS) Persistent Volume Storage 🌟](https://medium.com/@ershivamgupta/disaster-recovery-solution-for-azure-kubernetes-service-aks-persistent-volume-storage-f2b3d2aafcf4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@ershivamgupta: Disaster Recovery Solution for Azure Kubernetes' Service (AKS) Persistent Volume Storage 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/microsoftazure: Automating Managed Prometheus and Grafana with' Terraform for scalable observability on Azure Kubernetes Service and Istio 🌟](https://medium.com/microsoftazure/automating-managed-prometheus-and-grafana-with-terraform-for-scalable-observability-on-azure-4e5c5409a6b1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/microsoftazure: Automating Managed Prometheus and Grafana with' Terraform for scalable observability on Azure Kubernetes Service and Istio 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@GiantSwarm: Deep Dive Into Kubernetes Networking in Azure](https://medium.com/@GiantSwarm/deep-dive-into-kubernetes-networking-in-azure-9f0e85e2ee34)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@GiantSwarm: Deep Dive Into Kubernetes Networking in Azure in the Kubernetes Tools ecosystem.
  - [medium.com/@lfoster49203: Kubernetes on Azure: Setting up a cluster on Microsoft' Azure (with Azure AKS)](https://medium.com/@lfoster49203/kubernetes-on-azure-setting-up-a-cluster-on-microsoft-azure-with-azure-aks-d6bee3eaa65)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@lfoster49203: Kubernetes on Azure: Setting up a cluster on Microsoft' Azure (with Azure AKS) in the Kubernetes Tools ecosystem.
  - [medium.com/adessoturkey: Azure DevOps Agents on AKS with the kaniko Option](https://medium.com/adessoturkey/azure-devops-agents-on-aks-with-kaniko-option-f672f900a177)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/adessoturkey: Azure DevOps Agents on AKS with the kaniko Option in the Kubernetes Tools ecosystem.
  - [inder-devops.medium.com: AKS Networking Deep Dive: Kubenet vs Azure-CNI' vs Azure-CNI (overlay)](https://inder-devops.medium.com/aks-networking-deep-dive-kubenet-vs-azure-cni-vs-azure-cni-overlay-a51709171ce9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==inder-devops.medium.com: AKS Networking Deep Dive: Kubenet vs Azure-CNI' vs Azure-CNI (overlay)== in the Kubernetes Tools ecosystem.
  - [medium.com/@anjkeesari: Install Grafana Loki-Stack Helmchart in Azure Kubernetes' Services (AKS)](https://medium.com/@anjkeesari/install-grafana-loki-stack-helmchart-in-azure-kubernetes-services-aks-1359281b3321)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@anjkeesari: Install Grafana Loki-Stack Helmchart in Azure Kubernetes' Services (AKS) in the Kubernetes Tools ecosystem.
  - [blog.stackademic.com: Advanced End-to-End DevSecOps Kubernetes Three-Tier' Project using Azure AKS, fluxCD, Prometheus, Grafana, and GitLab](https://blog.stackademic.com/advanced-end-to-end-devsecops-kubernetes-three-tier-project-using-azure-aks-fluxcd-prometheus-cca3c5e61953)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.stackademic.com: Advanced End-to-End DevSecOps Kubernetes Three-Tier' Project using Azure AKS, fluxCD, Prometheus, Grafana, and GitLab in the Kubernetes Tools ecosystem.
  - [faun.pub: External Secret Operator on AKS (with Terraform) for Azure Key' Vault Integration (with Workload Identity)](https://faun.pub/external-secret-operator-on-aks-with-terraform-for-azure-key-vault-integration-with-workload-1d0c31082373)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: External Secret Operator on AKS (with Terraform) for Azure Key' Vault Integration (with Workload Identity) in the Kubernetes Tools ecosystem.
  - [blog.doit-intl.com: How to Set Up Multi-Cluster Load Balancing with GKE](https://blog.doit-intl.com/how-to-setup-multi-cluster-load-balancing-with-gke-4b407e1f3dff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.doit-intl.com: How to Set Up Multi-Cluster Load Balancing with GKE in the Kubernetes Tools ecosystem.
  - [medium: How to provision Kubernetes Cluster in GCP Cloud (K8s)? 🌟](https://medium.com/avmconsulting-blog/kubernetes-google-kubernetes-engine-gke-99abf912f912)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: How to provision Kubernetes Cluster in GCP Cloud (K8s)? 🌟 in the Kubernetes Tools ecosystem.
  - [faun.pub: How to automate the setup of a Kubernetes cluster on GCP](https://faun.pub/how-to-automate-the-setup-of-a-kubernetes-cluster-on-gcp-e97918bf41de)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: How to automate the setup of a Kubernetes cluster on GCP in the Kubernetes Tools ecosystem.
  - [medium.com/@glen.yu: Getting started with eBPF and Cilium on GKE](https://medium.com/@glen.yu/getting-started-with-ebpf-and-cilium-on-gke-6553c5d7e02a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@glen.yu: Getting started with eBPF and Cilium on GKE in the Kubernetes Tools ecosystem.
  - [medium.com/@glen.yu: NGINX Ingress or GKE Ingress?](https://medium.com/@glen.yu/nginx-ingress-or-gke-ingress-d87dd9db504c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@glen.yu: NGINX Ingress or GKE Ingress? in the Kubernetes Tools ecosystem.
  - [medium.com/google-developer-experts: Getting started with GKE Gateway controller](https://medium.com/google-developer-experts/getting-started-with-gke-gateway-controller-ee45c3bc8996)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/google-developer-experts: Getting started with GKE Gateway controller in the Kubernetes Tools ecosystem.
  - [medium.com/google-cloud: Monitoring Kubernetes Clusters on GKE (Google Container' Engine)](https://medium.com/google-cloud/gke-monitoring-84170ea44833)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/google-cloud: Monitoring Kubernetes Clusters on GKE (Google Container' Engine) in the Kubernetes Tools ecosystem.
  - [blog.devgenius.io: Explore API Priority and Fairness to Ease the Load of' the APIServer](https://blog.devgenius.io/explore-api-priority-and-fairness-to-ease-the-load-of-the-apiserver-a4fe9c4e7174)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.devgenius.io: Explore API Priority and Fairness to Ease the Load of' the APIServer in the Kubernetes Tools ecosystem.
  - [faun.pub: Make Your Kubernetes Cluster Highly Available and Fault Tolerant' 🌟](https://faun.pub/deploy-active-active-multi-region-kubernetes-cluster-with-terraform-f2652e43f47e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Make Your Kubernetes Cluster Highly Available and Fault Tolerant' 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@pbijjala: reCap: Kube vrs Cloud DNS in GKE](https://medium.com/@pbijjala/recap-kube-vrs-cloud-dns-in-gke-b8d1d407e00d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@pbijjala: reCap: Kube vrs Cloud DNS in GKE in the Kubernetes Tools ecosystem.
  - [medium.com/google-cloud: Ingress in Google Kubernetes Products](https://medium.com/google-cloud/ingress-in-google-kubernetes-products-f22ded21f4ed)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/google-cloud: Ingress in Google Kubernetes Products in the Kubernetes Tools ecosystem.
  - [medium.com/@pbijjala: Considerations for Hardening your GKE, a workload' perceptive](https://medium.com/@pbijjala/considerations-for-hardening-your-gke-a-workload-perceptive-943be26949d2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@pbijjala: Considerations for Hardening your GKE, a workload' perceptive in the Kubernetes Tools ecosystem.
  - [medium.com/@jjlakis: GCP Secret Manager with self-hosted Kubernetes](https://medium.com/@jjlakis/gcp-secret-manager-with-self-hosted-kubernetes-db35d01d65f0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@jjlakis: GCP Secret Manager with self-hosted Kubernetes in the Kubernetes Tools ecosystem.
  - [tech.loveholidays.com: GKE Multi-Cluster Services — one bad probe away from' disaster](https://tech.loveholidays.com/gke-multi-cluster-services-one-bad-probe-away-from-disaster-62051fafe84e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering tech.loveholidays.com: GKE Multi-Cluster Services — one bad probe away from' disaster in the Kubernetes Tools ecosystem.
  - [Looking for GPU Capacity ? DWS got you covered !](https://medium.com/zencore/looking-for-gpu-capacity-dws-got-you-covered-d736b8c63ba6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Looking for GPU Capacity ? DWS got you covered ! in the Kubernetes Tools ecosystem.
  - [medium.com/google-cloud: Understanding health checks in GKE & Gateway API](https://medium.com/google-cloud/understanding-health-checks-in-gke-gateway-api-1c89f82bfba8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/google-cloud: Understanding health checks in GKE & Gateway API in the Kubernetes Tools ecosystem.
  - [medium: Multizone Kubernetes and VPC Load Balancer Setup with terraform](https://medium.com/vmacwrites/multizone-kubernetes-and-vpc-load-balancer-setup-9664b3c9ea5d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Multizone Kubernetes and VPC Load Balancer Setup with terraform in the Kubernetes Tools ecosystem.
  - [Linode Kubernetes Engine (LKE)](https://www.linode.com/products/kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Linode Kubernetes Engine (LKE) in the Kubernetes Tools ecosystem.
  - [medium: Create Kubernetes Cluster Using Linode LKE](https://medium.com/codex/create-kubernetes-cluster-using-linode-lke-4f9c71d03a8d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Create Kubernetes Cluster Using Linode LKE in the Kubernetes Tools ecosystem.
  - [blog.ediri.io: DigitalOcean Kubernetes Challenge](https://blog.ediri.io/digitalocean-kubernetes-challenge)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.ediri.io: DigitalOcean Kubernetes Challenge in the Kubernetes Tools ecosystem.
  - [Banzai Cloud 🌟](https://banzaicloud.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Banzai Cloud 🌟 in the Kubernetes Tools ecosystem.
## Architecture and Design

### Microservices Design

#### Production AKS Deployment

  - **(2021)** [optisolbusiness.com: Implementing Microservices Architecture in AKS](https://www.optisolbusiness.com/insight/implementing-microservices-architecture-in-aks) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details blueprint designs for structural microservices running on AKS clusters. Reviews optimal container scaling, deployment strategies, and integration with container registries (ACR). Guides engineers on transforming multi-container apps into production-ready architectures.
### Serverless Migrations

#### Container Apps

  - **(2022)** [dev.to: Moving Azure Functions from AKS to Container Apps](https://dev.to/christle/moving-azure-functions-from-aks-to-container-apps-k60) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical migration post detailing the shift of Azure Functions from AKS (utilizing KEDA) into Azure Container Apps (ACA). Compares resource footprints, administration friction, and scale behaviors. Highly educational for choosing the correct serverless scale model.
## Architecture Blueprint

### Multi-Cloud and Azure

#### Infrastructure Design

  - **(2024)** [github.com/stephaneey/azure-and-k8s-architecture: Azure and K8s Architecture' 🌟](https://github.com/stephaneey/azure-and-k8s-architecture) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated open-source repository featuring detailed visual design maps and deployment blueprints for running enterprise-grade workloads on Azure and AKS. Demonstrates architectural patterns for network security zoning, private endpoints, DNS configuration, and highly isolated hub-and-spoke virtual networks.
## Cloud Infrastructure

### AWS

#### Container Orchestration

  - **(2023)** [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive comparing AWS ECS, EKS, and serverless container execution via AWS Fargate. Synthesizing live cloud architectural trends, it presents insights into financial management, operational simplicity, and dynamic resource scaling, mapping out the trade-offs of using managed VM pools versus completely serverless options.
  - **(2022)** [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform](https://www.clickittech.com/cloud-services/amazon-ecs-vs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This comprehensive comparison highlights the operational differences, cost implications, and architecture layouts of Amazon ECS versus Amazon EKS. EKS targets standard Kubernetes-based deployments requiring high portability, while ECS is a highly optimized, opinionated AWS native orchestrator designed for seamless integration.
  - **(2021)** [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed comparative analysis of scaling strategies between Amazon ECS and EKS clusters. The article walks through key operational considerations, including EC2 Auto Scaling Groups, Karpenter, cluster autoscalers, and resource utilization dynamics, highlighting how choice of orchestration influences microservices scale limits.
#### EKS and Container Orchestration

  - **(2026)** [**github.com/aws-ia/terraform-aws-eks-blueprints (examples) 🌟🌟🌟**](https://github.com/aws-ia/terraform-aws-eks-blueprints) <span class='md-tag md-tag--info'>⭐ 3024</span> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A production-ready collection of Terraform modules designed to accelerate Amazon EKS cluster deployments. Live Grounding highlights its architecture for bootstrapping clusters with essential add-ons like Karpenter, AWS Load Balancer Controller, and Prometheus. It represents the industry standard for declarative EKS infrastructure provisioning.
### Amazon EKS

#### ACK

  - **(2026)** [==AWS Controllers for Kubernetes (ACK) 🌟==](https://github.com/aws-controllers-k8s/community) <span class='md-tag md-tag--info'>⭐ 2627</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official community hub for AWS Controllers for Kubernetes (ACK). It allows cloud platform engineers to define and manage AWS resources (like RDS databases, S3 buckets, and SQS queues) directly through standard Kubernetes manifests and controllers.
#### Batch Workloads

  - **(2021)** [thenewstack.io: Amazon Web Services Gears Elastic Kubernetes Service for Batch Work](https://thenewstack.io/amazon-web-services-gears-elastic-kubernetes-service-for-batch-jobs) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes AWS EKS optimizations targeting high-performance batch computing and AI training workloads. It discusses integrations with Kueue, Karpenter, and specialized EC2 accelerator architectures designed to streamline modern machine learning cycles.
#### Cluster Provisioning

  - **(2021)** [hackerxone.com: 13 Steps Guide to Create Kubernetes Cluster on AWS](https://www.hackerxone.com/2021/08/20/13-steps-guide-to-create-kubernetes-cluster-on-amazon-web-serviceaws) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step procedural tutorial detailing manual and automated pathways to bootstrap a basic production-ready Amazon EKS cluster. Covers resource configuration, network VPC layouts, and kubectl integration.
  - **(2021)** [hackerxone.com: Steps to Create Amazon EKS node group on Amazon web Service (AWS)](https://www.hackerxone.com/2021/08/25/steps-to-create-amazon-eks-node-group-on-amazon-web-service-aws) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical guide to configuring, scaling, and associating managed node groups with existing Amazon EKS cluster control planes. It addresses instance type selection, IAM roles, and auto-scaling configurations.
  - **(2021)** [howtoforge.com: How to Create a Kubernetes Cluster with AWS CLI](https://www.howtoforge.com/how-to-create-a-kubernetes-cluster-with-the-aws-cli) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A basic command-line reference demonstrating how to script and provision AWS networking components, IAM dependencies, and EKS control planes directly through the AWS CLI.
#### Cost Optimization

  - **(2021)** [itnext.io: Deploy Kubernetes (K8s) on Amazon AWS using mixed on-demand and spot instances 🌟](https://itnext.io/deploy-kubernetes-k8s-on-amazon-aws-using-mixed-on-demand-and-spot-instances-5440e5bece7) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides engineers in orchestrating EKS worker pools featuring dynamic mixes of on-demand and spot instances. Investigates node affinity rules, taint strategies, and fallback mechanics designed to insulate workloads from spot termination spikes.
#### Deployments

  - **(2021)** [youtube/StackSimplify: Kubernetes Deployments on AWS EKS | Amazon Elastic Kubernetes Service | Amazon EKS 🌟](https://www.youtube.com/watch?v=vZK_W-fpft0&ab_channel=StackSimplify) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video-guided technical deep dive detailing how to launch and manage standard Kubernetes Deployments on AWS EKS. It covers declarative manifest configuration, pod scaling strategies, and external exposure of services through AWS integration.
#### Distributions

  - **(2021)** [linkedin.com: Amazon EKS Distro (EKS-D): The Kubernetes Distribution Used by Amazon EKS 🌟](https://www.linkedin.com/pulse/amazon-eks-distro-eks-d-kubernetes-distribution-used-gokul-chandra) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Amazon EKS Distro (EKS-D), the same open-source upstream Kubernetes distribution used by AWS to power Amazon EKS. The article highlights its value for on-premises deployments requiring the exact upstream patches, dependencies, and security alignments maintained by Amazon.
#### Helm Repositories

  - **(2026)** [==github.com/aws/eks-charts 🌟==](https://github.com/aws/eks-charts) <span class='md-tag md-tag--info'>⭐ 1298</span> <span class='md-tag md-tag--warning'>[SMARTY CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Helm chart repository maintained by Amazon Web Services to bootstrap essential cluster add-ons. It hosts deployment packages for core utilities like App Mesh Controller, AWS Load Balancer Controller, Node Termination Handler, and the VPC CNI plugin.
#### Interactive Learning

  - **(2026)** [eksworkshop.com 🌟](https://www.eksworkshop.com) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — The official Amazon EKS Workshop, serving as the industry's premier hands-on guide for EKS architecture. Updated consistently to reflect modern AWS paradigms, it leads operators through provisioning, networking (VPC CNI), security (IRSA), observability, and GitOps.
#### Observability

  - **(2022)** [aws.amazon.com: Troubleshooting Amazon EKS API servers with Prometheus](https://aws.amazon.com/de/blogs/containers/troubleshooting-amazon-eks-api-servers-with-prometheus) <span class='md-tag md-tag--warning'>[PROMQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses Prometheus instrumentation and query dashboards tailored specifically for evaluating EKS API server health. Analyzes performance bottlenecks, webhook latency, request queues, and resource utilization to maintain high availability.
  - **(2021)** [aws.amazon.com: Fluent Bit Integration in CloudWatch Container Insights for EKS](https://aws.amazon.com/blogs/containers/fluent-bit-integration-in-cloudwatch-container-insights-for-eks) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Analyzes the native integration of Fluent Bit within CloudWatch Container Insights for high-performance log routing in EKS. Live Grounding verifies this as the standard cloud-native pattern, replacing legacy Fluentd setups to achieve lower memory overhead and sub-millisecond log processing speeds.
  - **(2021)** [aws.amazon.com: Streaming Kubernetes Events in Slack](https://aws.amazon.com/blogs/containers/streaming-kubernetes-events-in-slack) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Walkthrough detailing how to set up serverless notification integration pipelines that stream Kubernetes events directly to Slack. Integrates tools like BotKube or AWS Lambda with EKS clusters to optimize developer response loops.
#### Spot Instances

  - **(2026)** [==aws/aws-node-termination-handler 🌟==](https://github.com/aws/aws-node-termination-handler) <span class='md-tag md-tag--info'>⭐ 1757</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — High-efficiency agent ensuring EKS pod rescheduling during abrupt EC2 instance maintenance events, Spot interruptions, or ASG rebalance recommendations. Gracefully drains affected nodes, maintaining overall cluster operational reliability.
#### Traffic Management

  - **(2022)** [Create a pipeline with canary deployments for Amazon EKS with AWS App Mesh 🌟](https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-eks-with-aws-app-mesh) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive technical walkthrough on implementing canary deployment pipelines using Amazon EKS and AWS App Mesh. It details the integration of AWS CodePipeline and Envoy-based service meshes to orchestrate fine-grained traffic shifting, minimizing blast radiuses during software rollouts.
### Auto-scaling

#### Fargate

  - **(2021)** [aws.amazon.com: Autoscaling EKS on Fargate with custom metrics](https://aws.amazon.com/blogs/containers/autoscaling-eks-on-fargate-with-custom-metrics) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores scaling mechanisms for EKS pods deployed onto AWS Fargate using Prometheus-emitted custom metrics. Illustrates HPA structures that scale serverless compute workloads without maintaining EC2 scaling profiles.
#### Prometheus

  - **(2021)** [aws.amazon.com: Using Prometheus Adapter to autoscale applications running on Amazon EKS](https://aws.amazon.com/blogs/mt/automated-scaling-of-applications-running-on-eks-using-custom-metric-collected-by-amazon-prometheus-using-prometheus-adapter) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to configure the Prometheus Adapter to expose custom application metrics to the Kubernetes Horizontal Pod Autoscaler (HPA). The article outlines ingestion pipelines from Amazon Managed Service for Prometheus to enable dynamic workload scaling.
### Cloud Migration

#### Automation

  - **(2026)** [==github.com/awslabs: Kubernetes Migration Factory User Guide 🌟==](https://github.com/awslabs/aws-kubernetes-migration-factory) <span class='md-tag md-tag--info'>⭐ 130</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The AWS Kubernetes Migration Factory provides an automated, programmatic framework for migrating legacy VM-based or on-premises workloads into Amazon EKS. Curator Insight notes its structured pipelines that reduce migration errors, while Live Grounding confirms its utility in enterprise-scale rehosting plans. Key features include source-to-target automation, pre-migration validation, and automated target cluster provisioning.
### Container Orchestration (1)

#### AKS Integration

  - **(2023)** [techcommunity.microsoft.com: How to install an AKS cluster with the Istio service mesh add-on via Bicep](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/how-to-install-an-aks-cluster-with-the-istio-service-mesh-add-on-via-bicep/3802069) <span class='md-tag md-tag--warning'>[BICEP CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the automated provisioning of Azure Kubernetes Service (AKS) coupled with the native Istio service mesh add-on using Bicep. This blueprint demonstrates declarative service mesh lifecycle management, reducing manual Helm or post-deployment orchestration overhead.
#### EKS Security

  - **(2023)** [Amazon EKS introduces EKS Pod Identity](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-eks-pod-identity) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — EKS Pod Identity simplifies the association of IAM roles with Kubernetes service accounts. This model bypasses the complexities of OIDC trust configurations, offering highly scalable, secure, and isolated credential structures for containers.
### Continuous Delivery

#### GitOps

  - **(2020)** [pages.awscloud.com: GitOps on AWS for High Performing Team Operations (eBook)](https://pages.awscloud.com/GLOBAL-partner-DL-DevOps-weaveworks-ebook-2020-learn.html) <span class='md-tag md-tag--warning'>[PDF CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An e-book co-authored by AWS and Weaveworks exploring the deployment of GitOps workflows on AWS. It presents architectural patterns for using declarative systems to synchronize desired states defined in Git with operational EKS environments.
#### Preview Environments

  - **(2022)** [thenewstack.io: How We Built Preview Environments on Kubernetes and AWS](https://thenewstack.io/how-we-built-preview-environments-on-kubernetes-and-aws) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural case study illustrating how to dynamically generate on-demand sandbox preview environments on AWS EKS. It outlines how custom controllers spin up ephemeral namespaces triggered by GitHub pull requests, improving QA workflows.
### Cost Optimization (1)

#### Best Practices

  - **(2022)** [cast.ai: 8 best practices to reduce your AWS bill for Kubernetes](https://cast.ai/blog/eks-cost-optimization) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical guide outlining eight proven vectors for optimizing AWS EKS spend. Recommendations highlight spot instance utilization, rightsizing CPU/memory allocations, automated pod pausing, and real-time scaling engines to eliminate compute waste.
#### Kubecost

  - **(2022)** [AWS and Kubecost collaborate to deliver cost monitoring for EKS customers](https://aws.amazon.com/blogs/containers/aws-and-kubecost-collaborate-to-deliver-cost-monitoring-for-eks-customers) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the native integration of Kubecost with Amazon EKS to provide free, high-granularity in-cluster resource cost allocations. Demonstrates how administrators trace expenditures back to namespaces, labels, and specific engineering departments.
### Infrastructure as Code

#### AWS CDK

  - **(2026)** [==aws-quickstart/cdk-eks-blueprints: Amazon EKS Blueprints for CDK==](https://github.com/awslabs/cdk-eks-blueprints) <span class='md-tag md-tag--info'>⭐ 510</span> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An AWS Cloud Development Kit (CDK) based framework that simplifies bootstrapping and configuring production-ready EKS clusters. Synthesizing developer insight with live deployment footprints, it provides programmatic control over EKS configurations, core add-ons, and IAM integrations. It is ideal for teams seeking TypeScript/Python program-based IaC over static YAML or HCL configurations.
  - **(2021)** [aws.amazon.com: Continuous Delivery of Amazon EKS Clusters Using AWS CDK and CDK Pipelines](https://aws.amazon.com/blogs/containers/continuous-delivery-of-amazon-eks-clusters-using-aws-cdk-and-cdk-pipelines) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights declarative automation pathways for bootstrapping EKS clusters using AWS Cloud Development Kit (CDK) Pipelines. Enables software engineering teams to manage clusters and infrastructure configurations as deployable programming code.
#### Terraform

  - **(2021)** [youtube: CloudGeeks - Terraform Eks Kubernetes RDS Secrets Manager Eksctl Cloudformation ALB Controller (Redmine App)](https://www.youtube.com/watch?v=OFZYIr66Ku4&ab_channel=cloudgeeksinc) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive practical video guide displaying multi-tier app deployment. Integrates Terraform, EKS, RDS, AWS Secrets Manager, and AWS ALB Controller to assemble an enterprise-grade cloud footprint.
### Multi-Cluster Management

#### Case Study

  - **(2021)** [Onfido’s Journey to a Multi-Cluster Amazon EKS Architecture](https://aws.amazon.com/blogs/containers/onfidos-journey-to-a-multi-cluster-amazon-eks-architecture) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Onfido's architectural transition from single-cluster configurations to a multi-region, multi-cluster Amazon EKS framework. Details scaling hurdles, network federation, load balancing, and configuration management at global enterprise scale.
#### Rancher

  - **(2021)** [Optimizing Your Kubernetes Clusters with Rancher and Amazon EKS 🌟](https://aws.amazon.com/blogs/apn/optimizing-your-kubernetes-clusters-with-rancher-and-amazon-eks) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the integration of SUSE Rancher with Amazon EKS to simplify multi-cluster operations. Curator Insight notes its focus on centralizing security policies, while Live Grounding highlights its architecture for consolidating hybrid-cloud operations and unified access controls across distributed clusters.
### Networking

#### Best Practices (1)

  - **(2026)** [Amazon EKS Best Practices Guide for Networking](https://aws.github.io/aws-eks-best-practices/networking/index) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The dedicated guide for networking best practices on Amazon EKS. Focuses heavily on network design, security boundaries, container security, network policies (Calico), and optimizing cluster communication pathways.
#### Ingress Controllers

  - **(2026)** [==github.com/kubernetes-sigs/aws-load-balancer-controller==](https://github.com/kubernetes-sigs/aws-load-balancer-controller) <span class='md-tag md-tag--info'>⭐ 4300</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The core controller that manages AWS Elastic Load Balancers (ALB and NLB) on behalf of a Kubernetes cluster. Live Grounding verifies its continuous support for advanced features like target grouping by IP, ACM certificate integration, and shared ALBs. It acts as the primary ingress controller for modern AWS EKS network architectures.
  - **(2024)** [AWS Load Balancer Controller 🌟](https://kubernetes-sigs.github.io/aws-load-balancer-controller) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documentation focused on integrating the AWS Load Balancer Controller with ExternalDNS. This pattern automates Route 53 DNS record creation and synchronization when ALBs or NLBs are dynamically provisioned via Kubernetes Ingress or Service resources.
  - **(2021)** [aws.amazon.com: Kubernetes Ingress with AWS ALB Ingress Controller](https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Covers the deployment and usage architecture of the AWS Application Load Balancer (ALB) Ingress Controller. It shows how the controller interprets Kubernetes Ingress resources to provision physical AWS ALB layers, routing external HTTP traffic directly to backend pods.
#### Scale Optimization

  - **(2022)** [engineering.salesforce.com: Optimizing EKS networking for scale](https://engineering.salesforce.com/optimizing-eks-networking-for-scale-1325706c8f6d) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical case study detailing Salesforce's optimizations of the AWS VPC CNI within high-density EKS clusters. It addresses IP address exhaustion, custom networking configurations, prefix delegation, and scaling metrics crucial for maintaining thousands of ephemeral microservices.
  - **(2022)** [dev.to: One technique to save your AWS EKS IP addresses 10x](https://dev.to/timtsoitt/one-technique-to-save-your-aws-eks-ip-addresses-10x-2ocn) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights optimization tips for saving IP configurations on AWS EKS nodes. Describes how prefix delegation settings on the VPC CNI plug-in reduce IP wastage on EC2 network cards, avoiding standard subnet depletion issues.
### Reliability Engineering

#### Chaos Engineering

  - **(2021)** [thenewstack.io: Deploy Gremlin to Amazon EKS Using AWS CloudFormation](https://thenewstack.io/deploy-gremlin-to-amazon-eks-using-aws-cloudformation) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to orchestrate the deployment of the Gremlin chaos engineering agent across EKS worker nodes using CloudFormation. The setup helps operators proactively identify infrastructure failure modes through controlled agent-driven network and CPU stress tests.
### Security and Compliance

#### Best Practices (2)

  - **(2022)** [cast.ai: EKS Security Checklist: 10 Best Practices for a Secure Cluster](https://cast.ai/blog/eks-security-checklist-10-best-practices-for-a-secure-cluster) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A security verification checklist designed for EKS. Evaluates API network isolation, node-level hardenings, RBAC, KMS secret encryption, and runtime defense models necessary to pass enterprise audits.
#### IAM

  - **(2026)** [==azon EKS Pod Identity Webhook==](https://github.com/aws/amazon-eks-pod-identity-webhook) <span class='md-tag md-tag--info'>⭐ 683</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A mutating admission webhook that injects AWS IAM environmental variables and credentials into Kubernetes Pods. This enables IAM Roles for Service Accounts (IRSA), allowing pods to securely access external AWS API endpoints without relying on shared node-level roles.
  - **(2022)** [nextlinklabs.com: Handling Auth in EKS Clusters: Setting Up Kubernetes User Access Using AWS IAM](https://nextlinklabs.com/resources/insights/handling-authentication-in-eks-clusters-kubernetes-aws-iam) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A procedural analysis on managing administrative and developer user access to Amazon EKS using AWS IAM and the aws-auth ConfigMap. It maps IAM roles and users to internal Kubernetes RBAC groups, ensuring fine-grained, secure administrative control.
  - **(2021)** [dev.to: EKS IAM Deep Dive 🌟](https://dev.to/aws-builders/eks-iam-deep-dive-136d) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth exploration of the security layer connecting AWS Identity and Access Management with EKS. Details authentication and authorization, explaining how IAM roles map to Kubernetes groups to achieve a robust security boundary.
#### PCI DSS

  - **(2020)** [aws whitepapers: Architecting Amazon EKS for PCI DSS Compliance (pdf) 🌟🌟](https://d1.awsstatic.com/whitepapers/architecting-amazon-eks-for-pci-dss-compliance.pdf) <span class='md-tag md-tag--warning'>[PDF CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An authoritative AWS whitepaper providing rigorous architectural guidelines for running Payment Card Industry Data Security Standard (PCI DSS) workloads on EKS. It focuses on network isolation, encryption at rest/transit, IAM control planes, and auditable logging configurations.
#### Policy Enforcement

  - **(2021)** [aws.amazon.com: Easy as one-two-three policy management with Kyverno on Amazon EKS 🌟](https://aws.amazon.com/blogs/containers/easy-as-one-two-three-policy-management-with-kyverno-on-amazon-eks) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the deployment of Kyverno on Amazon EKS to enforce policy as code using native Kubernetes resources. It demonstrates how to write policies to restrict root privileges, mutate incoming resources, and audit cluster compliance directly without writing complex Rego code.
### Storage

#### Amazon EFS

  - **(2021)** [aws.amazon.com: Mount Amazon EFS file systems cross-account from Amazon EKS, and utilize AWS Organizations more effectively](https://aws.amazon.com/blogs/storage/mount-amazon-efs-file-systems-cross-account-from-amazon-eks) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A guide to mounting Amazon Elastic File System (EFS) across separate AWS accounts using AWS Organizations and EKS. Outlines IAM policy delegation and EFS CSI driver setup to enable persistent shared storage across multi-tenant environments.
## Cloud Native

### AWS EKS

#### Cluster Provisioning (1)

  - **(2024)** [**eksctl: EKS installer**](https://github.com/eksctl-io/eksctl) <span class='md-tag md-tag--info'>⭐ 5203</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official CLI orchestration tool for provisioning AWS EKS clusters. It compiles high-level YAML inputs into CloudFormation actions to automatically establish VPC, IAM, and worker nodes.
  - **(2018)** [POKE - Provision Opinionated Kubernetes on EKS](https://github.com/bit-cloner/poke) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Opinionated CLI provisioning script wrapper for configuring standardized Amazon EKS instances. This project has been classified as legacy due to extensive inactivity; modern teams should leverage Terraform or EKS Blueprints instead.
#### Community Resources

  - **(2023)** [community.aws/kubernetes](https://builder.aws.com/learn/topics/kubernetes)  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Curated developer platform presenting technical walk-throughs, AWS integrations, architecture guides, and emerging patterns specifically centered around EKS and cloud-native topologies on AWS.
#### Cost Optimization (2)

  - **(2020)** [Running spot instances effectively with Amazon EKS](https://signalvnoise.com/svn3/running-spot-instances-effectively-with-amazon-eks) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Real-world operational strategies for utilizing cost-efficient Spot Instances under EKS. Covers node drain handling, spot termination alerts, and managing mixed instance type node groups.
  - **(2020)** [Amazon EKS Price Reduction](https://aws.amazon.com/blogs/aws/eks-price-reduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS announcement lowering the baseline cost of managing the EKS control plane. Outlines operational cost structures for running enterprise Kubernetes topologies at scale.
#### High Availability

  - **(2021)** [aws.amazon.com: Operating a multi-regional stateless application using Amazon EKS](https://aws.amazon.com/blogs/containers/operating-a-multi-regional-stateless-application-using-amazon-eks) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural whitepaper addressing how to design, deploy, and synchronize global stateless applications across multiple regional EKS clusters utilizing Route 53 routing policies.
#### Machine Learning

  - **(2020)** [Amazon EKS Now Supports EC2 Inf1 Instances](https://aws.amazon.com/blogs/aws/amazon-eks-now-supports-ec2-inf1-instances) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Product release covering EKS node compatibility with AWS Inferentia (Inf1) instances, enabling highly efficient, GPU-optimized hardware accelerations for deep learning and machine learning workloads on Kubernetes.
#### Multi-tenancy

  - **(2022)** [clickittech.com: Kubernetes Multi tenancy with Amazon EKS: Best practices and considerations](https://www.clickittech.com/devops/kubernetes-multi-tenancy) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Strategy guide mapping namespaces, NetworkPolicies, RBAC profiles, and network-level compute segmentation strategies to implement robust multi-tenant environments on AWS EKS.
#### Networking (1)

  - **(2022)** [stacksimplify.com: AWS ALB Ingress Service - Basics 🌟](https://docs.stacksimplify.com/aws-eks/aws-alb-ingress/lean-kubernetes-aws-alb-ingress-basics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Fundamentals on deploying the AWS Load Balancer Controller within EKS. Details mapping of ingress objects to physical Application Load Balancers, target groups, and routing configurations.
  - **(2021)** [itnext.io: Using AWS NLB manually targeting an EKS Service exposing UDP traffic](https://itnext.io/using-aws-nlb-manually-targeting-an-eks-service-exposing-udp-traffic-17053ecd8f52) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Advanced engineering tutorial outlining the manual provisioning and targeting configurations of Network Load Balancers (NLB) to handle inbound UDP traffic natively to pod layers on EKS.
#### Operator Pattern

  - **(2020)** [Announcing the AWS Controllers for Kubernetes Preview](https://aws.amazon.com/about-aws/whats-new/2020/08/announcing-the-aws-controllers-for-kubernetes-preview) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical release note for AWS Controllers for Kubernetes (ACK), allowing developers to provision and manage AWS managed services directly using Kubernetes custom resources and controller reconcile loops.
#### Security

  - **(2022)** [Amazon EKS Security Best Practices](https://www.stackrox.io/blog/amazon-eks-security-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive security manual focusing on EKS cluster isolation strategies. Discusses IAM Roles for Service Accounts (IRSA), security groups per pod, and control plane API exposure minimization.
  - **(2021)** [EKS Service Accounts Explained](https://fika.works/blog/eks-service-accounts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — In-depth analysis of IAM Roles for Service Accounts (IRSA) architecture. Covers OpenID Connect (OIDC) federation, JWT token injection, and structural principal boundary configuration.
#### Storage Solutions

  - **(2021)** [thenewstack.io: Install and Configure OpenEBS on Amazon Elastic Kubernetes Service](https://thenewstack.io/tutorial-install-and-configure-openebs-on-amazon-elastic-kubernetes-service) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical tutorial on running OpenEBS as a local containerized block storage provider within Amazon EKS node groups, optimizing performance for persistent enterprise workloads.
  - **(2021)** [Kubernetes PVCs with EFS provisioner](https://www.theodo.com/en-fr/blog/how-to-use-kubernetes-pvcs-with-efs-provisioner)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical configuration guide highlighting AWS EFS CSI driver setup to enable multi-attach ReadWriteMany (RWX) volumes across distributed stateful pods in Amazon EKS.
### Kubernetes

#### Architecture Design

  - **(2021)** [redhat.com: What architects need to know about managed Kubernetes](https://www.redhat.com/en/blog/managed-kubernetes-architects) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural breakdown addressing governance models, multi-cluster federation concerns, integration points, and overall vendor lock-in vectors for managed Kubernetes solutions.
#### Industry Trends

  - **(2021)** [infoworld.com: CNCF survey: Managed Kubernetes becomes the norm](https://www.infoworld.com/article/2334477/cncf-survey-managed-kubernetes-becomes-the-norm.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Industry report analyzing CNCF survey results, validating the near-ubiquitous transition of enterprise container orchestration towards public cloud managed control planes.
#### Managed Services

  - **(2022)** [infoworld.com: 6 reasons to switch to managed Kubernetes](https://www.infoworld.com/article/2264256/6-reasons-to-switch-to-managed-kubernetes.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Executive evaluation explaining the strategic operations shift from self-managed vanilla Kubernetes clusters to public cloud provider solutions like EKS, AKS, and GKE.
  - **(2022)** [armosec.io: Which Managed Kubernetes Is Right for Me?](https://www.armosec.io/blog/which-managed-kubernetes-is-right-for-me)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Security-focused landscape analysis comparing AWS EKS, Azure AKS, and Google Cloud GKE features with respect to security postures, compliance baselines, and control planes.
  - **(2022)** [youtube: Kubernetes Comparison](https://www.youtube.com/watch?v=xM9jpcVGTzY)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual and technical comparison analyzing installation friction, upgrade orchestration, custom configuration options, and managed-service limits for enterprise architectures.
  - **(2021)** [dev.to/thenjdevopsguy: AKS vs EKS vs GKE](https://dev.to/thenjdevopsguy/aks-vs-eks-vs-gke-2459)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Pragmatic, direct comparison evaluating deployment pipelines, networking models, pricing tiers, and tooling integrations across Azure, AWS, and GCP managed offerings.
  - **(2021)** [acloudguru.com: AKS vs EKS vs GKE: Managed Kubernetes services compared](https://www.pluralsight.com/resources/blog/cloud/aks-vs-eks-vs-gke-managed-kubernetes-services-compared)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Educational comparison targeting operations teams, reviewing storage performance, networking setups, and billing strategies across AWS, GCP, and Azure.
#### Platform Engineering

  - **(2021)** [thenewstack.io: Otomi Container Platform Offers an Integrated Kubernetes Bundle](https://thenewstack.io/otomi-container-platform-offers-an-integrated-kubernetes-bundle) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Product overview of Otomi, which bundles ingress, security benchmarks, network policies, monitoring tools, and service mesh components into a unified, installable suite for Kubernetes.
## Cloud Native and Kubernetes

### Monitoring and Observability

#### Network Observability

  - **(2024)** [**techcommunity.microsoft.com: Advanced Network Observability for your Azure Kubernetes Service clusters through Azure Monitor**](https://techcommunity.microsoft.com/blog/azureobservabilityblog/advanced-network-observability-for-your-azure-kubernetes-service-clusters-throug/4176736) <span class='md-tag md-tag--warning'>[KQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Unveiling advanced network observability features for AKS clusters, utilizing eBPF to capture kernel-level network telemetry. It provides deep visibility into pod-to-pod and egress traffic flow, packet drops, DNS resolution latencies, and TCP connection stats. This low-overhead monitoring is essential for debugging transient network issues inside microservices environments.
## Cloud Providers

### AWS EKS (1)

#### Cluster Lifecycle

##### Managed Add-ons

  - **(2023)** [docs.aws.amazon.com: Managing Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official operational documentation for administering lifecycle updates, configurations, and IAM permissions of core Amazon EKS add-ons. Simplifies the lifecycle management of essential operational software such as CoreDNS, kube-proxy, and the VPC CNI.
##### Node Updates

  - **(2023)** [Updating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/update-managed-node-group.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Complete operational reference for rolling out Kubernetes version updates and AMI revisions across AWS Managed Node Groups. Focuses on graceful drain orchestration and node surge strategies to maintain active service availability.
##### Upgrade Strategies

  - **(2023)** [aws.amazon.com: Planning Kubernetes Upgrades with Amazon EKS](https://aws.amazon.com/blogs/containers/planning-kubernetes-upgrades-with-amazon-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A strategic framework for executing major Kubernetes cluster version migrations on Amazon EKS. Outlines lifecycle calendars, API deprecation checkpoints, testing environments, and emergency rollback procedures for production platforms.
##### Upgrade Strategy

  - **(2023)** [repost.aws: How do I plan an upgrade strategy for an Amazon EKS cluster?](https://repost.aws/knowledge-center/eks-plan-upgrade-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An operational walkthrough guiding cluster operators through step-by-step diagnostic and execution checklists for upgrading an EKS control plane and worker nodes while verifying structural API compatibility.
#### Cost Optimization (3)

##### Node Scaling Metrics

  - **(2023)** [**awslabs/eks-node-viewer**](https://github.com/awslabs/eks-node-viewer) <span class='md-tag md-tag--info'>⭐ 1632</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly functional CLI diagnostic tool designed to visualize real-time cost, resource utilization, and scheduling efficiency across Amazon EKS node groups. Highly integrated with dynamic autoscaling engines like Karpenter to optimize infrastructure financial footprints.
##### Spot Instancing

  - **(2022)** [itnext.io: Running resilient workloads in EKS using Spot instances](https://itnext.io/running-production-workloads-in-eks-using-spot-instances-fc6808a7b462) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical implementation guide for orchestrating highly available production applications on cost-effective AWS Spot Instances. Synthesizes node-termination handlers, pod disruption budgets, and multi-instance-type autoscaling groups to manage interruptions.
#### GitOps and Automation

##### Infrastructure Provisioning

  - **(2023)** [aws.amazon.com: GitOps model for provisioning and bootstrapping Amazon EKS clusters using Crossplane and Argo CD](https://aws.amazon.com/blogs/containers/gitops-model-for-provisioning-and-bootstrapping-amazon-eks-clusters-using-crossplane-and-argo-cd) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates an elegant architectural GitOps paradigm that unifies cloud infrastructure and software delivery. Integrates Crossplane for declarative AWS API provisioning with Argo CD for continuous application state synchronizations.
#### Hybrid Cloud

##### Blue-Green Upgrades

  - **(2022)** [aws.amazon.com: Blue/Green Kubernetes upgrades for Amazon EKS Anywhere using Flux](https://aws.amazon.com/blogs/containers/blue-green-kubernetes-upgrades-for-amazon-eks-anywhere-using-flux) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Showcases a robust GitOps upgrading mechanism using Flux CD on EKS Anywhere clusters. Focuses on orchestrating safe blue/green cluster migrations to minimize physical infrastructure interruptions.
##### Feature Matrix

  - **(2022)** [anywhere.eks.amazonaws.com: Compare EKS Anywhere and EKS](https://anywhere.eks.amazonaws.com/docs/concepts/eksafeatures) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structural feature matrix comparing EKS Anywhere and standard AWS-hosted EKS. Analyzes governance models, infrastructure obligations, software component differences, and target workload environments.
##### Getting Started

  - **(2021)** [aws.amazon.com: Getting started with Amazon EKS Anywhere](https://aws.amazon.com/blogs/containers/introducing-general-availability-of-amazon-eks-anywhere) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Fundamental provisioning guide to instantiate an EKS Anywhere sandbox cluster. Leverages Docker-based local execution to demonstrate the configuration profiles and administration scripts of local EKS-compliant architectures.
##### On-Premises EKS

  - **(2023)** [**EKS Anywhere: github.com/aws/eks-anywhere**](https://github.com/aws/eks-anywhere) <span class='md-tag md-tag--info'>⭐ 2096</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Official hybrid-cloud open-source distribution bringing EKS lifecycle tooling, operational practices, and configurations directly into bare-metal, vSphere, or Nutanix environments. Maintains uniform operational patterns across hybrid infrastructures.
##### On-Premises Launch

  - **(2021)** [aws.amazon.com: Amazon EKS Anywhere – Now Generally Available to Create and Manage Kubernetes Clusters on Premises](https://aws.amazon.com/blogs/aws/amazon-eks-anywhere-now-generally-available-to-create-and-manage-kubernetes-clusters-on-premises) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Launches EKS Anywhere into general availability, introducing key hybrid cloud deployment architectures. Examines how on-premises teams can leverage automated OS patching, tooling uniformity, and professional AWS support channels.
##### Service Mesh Integration

  - **(2022)** [solo.io: Connect Your Services Seamlessly with Amazon EKS Anywhere and Istio](https://www.solo.io/blog/amazon-eks-anywhere-and-solo-istio) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on extending enterprise network topologies and security controls to the hybrid-edge using Solo Gloo Mesh (Istio) over EKS Anywhere nodes. Streamlines cross-cloud security boundaries and load balancing profiles.
#### Infrastructure as Code (1)

##### NFS Storage Autoprovisioning

  - **(2022)** [dev.to: Autoprovisioning NFS volumes in EKS with CDK](https://dev.to/memark/autoprovisioning-nfs-volumes-in-eks-with-cdk-4fn9) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walks through the automated provisioning of NFS-backed persistent storage within Amazon EKS utilizing the AWS Cloud Development Kit (CDK). Demonstrates infrastructure-as-code automation for deploying NFS CSI drivers and configuring storage classes.
#### Kubernetes Distributions

##### Base Build

  - **(2023)** [aws/eks-distro](https://github.com/aws/eks-distro) <span class='md-tag md-tag--info'>⭐ 1458</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source release containing the exact upstream Kubernetes components, security backports, and upstream patches used by Amazon EKS. Empowers platform developers to run highly synchronized non-AWS clusters.
#### Machine Learning (1)

##### Kubeflow Storage

  - **(2022)** [aws.amazon.com: Machine Learning with Kubeflow on Amazon EKS with Amazon EFS](https://aws.amazon.com/blogs/storage/machine-learning-with-kubeflow-on-amazon-eks-with-amazon-efs) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Illustrates the reference architecture for scaling distributed machine learning workloads using Kubeflow on Amazon EKS backed by AWS EFS. Addresses shared-storage patterns crucial for training datasets, model checkpoints, and collaborative Jupyter notebooks.
#### Monitoring and Observability (1)

##### API Server Diagnostics

  - **(2022)** [aws.amazon.com: Troubleshooting Amazon EKS API servers with Prometheus and Grafana](https://aws.amazon.com/blogs/containers/troubleshooting-amazon-eks-api-servers-with-prometheus) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural guide for diagnosing Amazon EKS API server performance using metrics scraped by Prometheus and rendered via Grafana dashboards. Explains how to identify bottlenecks like throttling, request latency, and resource starvation in managed control planes.
#### Networking (2)

##### CoreDNS Scaling

  - **(2024)** [aws.amazon.com: Amazon EKS announces native support for autoscaling CoreDNS Pods](https://aws.amazon.com/about-aws/whats-new/2024/05/amazon-eks-native-support-autoscaling-coredns-pods) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the native capabilities of EKS to automatically configure horizontal scaling for CoreDNS deployments based on cluster scale metrics. Solves structural DNS performance bottlenecks during massive scaling events without custom cron jobs.
##### IP Management

  - **(2022)** [aws.amazon.com: Addressing IPv4 address exhaustion in Amazon EKS clusters using private NAT gateways](https://aws.amazon.com/blogs/containers/addressing-ipv4-address-exhaustion-in-amazon-eks-clusters-using-private-nat-gateways) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Proposes a highly scalable network topology to mitigate RFC 1918 IPv4 exhaustion in large-scale EKS clusters. Describes configuring private NAT Gateways and secondary VPC CIDRs to decouple internal pod networking from restricted corporate network spaces.
##### Private Connectivity

  - **(2022)** [docs.aws.amazon.com: Access container applications privately on Amazon EKS using AWS PrivateLink and a Network Load Balancer](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-eks-using-aws-privatelink-and-a-network-load-balancer.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed architectural pattern showcasing secure, private consumption of containerized applications deployed on Amazon EKS. Leverages AWS PrivateLink integrated with a Network Load Balancer (NLB) to isolate traffic from the public internet entirely.
##### Service Mesh Latency

  - **(2023)** [aws.amazon.com: Addressing latency and data transfer costs on EKS using Istio](https://aws.amazon.com/blogs/containers/addressing-latency-and-data-transfer-costs-on-eks-using-istio) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural guide analyzing multi-AZ data transfer charges and service-to-service latency in EKS. Demonstrates how to design topology-aware routing strategies within an Istio Service Mesh to keep traffic localized and cost-effective.
#### Scalability

##### Image Prefetching

  - **(2023)** [aws.amazon.com: Start Pods faster by prefetching images](https://aws.amazon.com/blogs/containers/start-pods-faster-by-prefetching-images) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Describes the container image prefetching architecture on EKS nodes to slash cold-start initialization latency. Discusses daemonset solutions, caching strategies, and optimizing node startup times for responsive, highly dynamic cluster configurations.
##### Proactive Scaling

  - **(2022)** [Eliminate Kubernetes node scaling lag with pod priority and over-provisioning](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Examines the design pattern of utilizing low-priority 'placeholder' pods to pre-provision infrastructure capacity on EKS clusters. Ensures that traffic spikes or high-priority deployments are scheduled instantly without waiting for node boot cycles.
##### Stateful Databases

  - **(2022)** [Scaling Amazon EKS and Cassandra Beyond 1,000 Nodes](https://aws.amazon.com/blogs/containers/scaling-amazon-eks-and-cassandra-beyond-1000-nodes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical retrospective documenting the extreme scale performance testing of Cassandra clusters across 1,000+ nodes on EKS. Highlights optimal kernel-level tuning, persistent storage layout modifications, and scheduler fine-tuning required to maintain stateful reliability.
#### Security and Hardening

##### Compliance Auditing

  - **(2023)** [aws-samples/hardeneks](https://github.com/aws-samples/hardeneks) <span class='md-tag md-tag--info'>⭐ 958</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A command-line verification tool that systematically audits Amazon EKS clusters against established AWS operational and security best practices. Evaluates network security, IAM posture, pod disruption budgets, and admission control policies to generate a structured hardening roadmap.
##### RBAC Mapping

  - **(2023)** [itnext.io: AWS Elastic Kubernetes Service: RBAC Authorization via AWS IAM and RBAC Groups](https://itnext.io/aws-elastic-kubernetes-service-rbac-authorization-via-aws-iam-and-rbac-groups-7b70ded144b5) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep technical review of orchestrating native Kubernetes Role-Based Access Control (RBAC) securely mapped to AWS IAM roles. Details operational best practices for mapping IAM identities into the aws-auth ConfigMap or using EKS Access Entries.
##### Ransomware Defense

  - **(2023)** [itnext.io: Top 10 Ways to Protect EKS Workloads from Ransomware](https://itnext.io/top-10-ways-to-protect-eks-workloads-from-ransomware-ae96d1c1e839) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Aggregates critical tactical recommendations to defend EKS environments from ransomware vectors. Covers immutability configurations for persistent volumes, robust IAM role isolation, network policies, and scanning container images within CI/CD loops.
#### Storage (1)

##### EBS Migration

  - **(2023)** [Simplifying Amazon EBS volume migration and modification on Kubernetes using the EBS CSI Driver](https://aws.amazon.com/de/blogs/storage/simplifying-amazon-ebs-volume-migration-and-modification-using-the-ebs-csi-driver) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines techniques for non-disruptively scaling, upgrading, and migrating stateful persistent volumes using the advanced AWS Elastic Block Store (EBS) CSI Driver. Focuses on hot-modifying volume sizes, IOPS parameters, and throughput.
##### Persistent Volumes

  - **(2021)** [aws.amazon.com: Persistent storage for Kubernetes](https://aws.amazon.com/blogs/storage/persistent-storage-for-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive architectural assessment of persistent storage paradigms in AWS-hosted Kubernetes. Contrasts EBS, EFS, and FSx for Lustre, outlining optimal use cases, performance characteristics, and mounting protocols across containerized applications.
### Azure Kubernetes Service AKS

#### API Gateway

  - **(2023)** [returngis.net: Exponer APIs en AKS a través de Azure API Management](https://www.returngis.net/2023/05/exponer-apis-en-aks-a-traves-de-azure-api-management) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a hands-on architectural walkthrough for exposing microservices deployed on AKS through Azure API Management (APIM). Focuses on securing internal endpoints via private virtual network injection, setting up private DNS zones, and orchestrating ingress paths with NGINX or AGIC. Essential reading for configuring robust API monetization and rate-limiting behaviors.
#### Autoscaling

  - **(2023)** [pixelrobots.co.uk: Exploring Azure Kubernetes Service’s Node Autoprovision: A Deep Dive into the Latest Public Preview Feature](https://pixelrobots.co.uk/2023/12/exploring-azure-kubernetes-services-node-autoprovision-a-deep-dive-into-the-latest-public-preview-feature) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth review of AKS Node Autoprovisioning (NAP), an implementation based on the open-source Karpenter project. NAP evaluates unschedulable pod manifests to dynamically provision the optimal VM sizes and SKU mixtures, circumventing the constraints of static Kubernetes Node Pools. Highly relevant for architects looking to decrease scaling latency and infrastructure wastage.
#### Community Updates

  - **(2024)** [dinantpaardenkooper.nl: Azure Day with Kubernetes](https://dinantpaardenkooper.nl/posts/aks-2024-03-18) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synthesizes major engineering takeaways, cluster management trends, and updates shared at the Azure Day with Kubernetes community event. Focuses on practical engineering realities, real-world troubleshooting, and evolving cloud-native tooling within the AKS landscape.
#### Edge Computing

  - **(2023)** [thenewstack.io: Microsoft Takes Kubernetes to the Edge with AKS Lite](https://thenewstack.io/microsoft-takes-kubernetes-to-the-edge-with-aks-lite) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the release and architecture of AKS Edge Essentials, a lightweight managed Kubernetes platform designed to run nested workloads on Windows IoT and edge hardware. Focuses on minimal hardware footprint requirements, local network routing, and continuous integration with centralized Azure Arc control planes.
#### Enterprise Design Patterns

  - **(2024)** [learn.microsoft.com: AKS landing zone accelerator](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/aks/landing-zone-accelerator) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The definitive AKS Landing Zone Accelerator framework aligned with the Microsoft Cloud Adoption Framework (CAF). Provides production-ready templates and structural guidelines covering networking topologies (hub-and-spoke), subscription governance, unified identity management, and default security baselines. This reference is crucial for bootstrapping compliant, enterprise-grade managed Kubernetes environments.
#### High Availability (1)

  - **(2024)** [techcommunity.microsoft.com: A Practical Guide to Zone Redundant AKS Clusters and Storage](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/a-practical-guide-to-zone-redundant-aks-clusters-and-storage/4036254) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical reference guide focused on designing zone-redundant AKS clusters and resolving multi-zone storage constraints. Addresses the architectural differences between zone-redundant storage (ZRS) and locally redundant storage (LRS) when backing Kubernetes persistent volumes. It maps failure-domain behavior and node affinity to ensure stateful workloads remain resilient to physical datacenter outages.
#### Identity and Access Control

  - **(2024)** [techcommunity.microsoft.com: Simplifying Azure Kubernetes Service Authentication Part 2](https://techcommunity.microsoft.com/blog/appsonazureblog/simplifying-azure-kubernetes-service-authentication-part-2/4055332) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — This architectural technical review breaks down modern AKS authentication structures. Demonstrates how to configure Microsoft Entra ID integration with native Kubernetes RBAC, manage token lifecycles with kubelogin, and enforce administrative access groups. Eliminates security anti-patterns associated with legacy static admin kubeconfigs.
#### Ingress and Routing

  - **(2023)** [returngis.net: Desplegar AGIC en AKS utilizando workload identity](https://www.returngis.net/2023/05/desplegar-agic-en-aks-utilizando-workload-identity) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A deep dive into deploying the Azure Application Gateway Ingress Controller (AGIC) utilizing passwordless Azure AD Workload Identity instead of legacy pod-managed identity options. By using OpenID Connect (OIDC) federation, this design model mitigates key-rotation liabilities and secures the control plane path to application gateways. This configuration represents the de facto standard for zero-trust ingress security on Azure.
#### Machine Learning Workloads

  - **(2024)** [techcommunity.microsoft.com: Running GPU accelerated workloads with NVIDIA GPU Operator on AKS 🌟](https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/running-gpu-accelerated-workloads-with-nvidia-gpu-operator-on-aks/4061318) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An enterprise guide for orchestrating GPU-accelerated workloads on AKS via the NVIDIA GPU Operator. Covers automating driver configuration, runtime modifications, and hardware telemetry. This blueprint enables reliable execution of machine learning, AI model training, and heavy mathematical modeling pipelines inside container runtimes.
#### Multi-Tenancy

  - **(2024)** [learn.microsoft.com: Use Application Gateway Ingress Controller (AGIC) with a multitenant Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/aks-agic/aks-agic) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This official reference architecture outlines deployment scenarios for using AGIC within multi-tenant AKS cluster designs. It synthesizes strategies for shared vs. dedicated Application Gateways, details path-based and host-based microservices routing, and outlines how to securely terminate TLS while enforcing Web Application Firewall (WAF) rule sets at the perimeter.
#### Observability (1)

  - **(2024)** [learn.microsoft.com: Monitor Azure Kubernetes Service (AKS) control plane metrics (preview)](https://learn.microsoft.com/en-us/azure/aks/monitor-aks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to monitor managed AKS control plane metrics using the Prometheus-compatible Azure Monitor Workspace. Surfacing vital indicators like API server latency, workqueue depth, and etcd operations, this feature enables SRE teams to identify cluster orchestration bottlenecks and validate control plane scalability during massive pod churn events.
#### Onboarding

  - **(2024)** [piotrminkowski.com: Getting Started with Azure Kubernetes Service 🌟](https://piotrminkowski.com/2024/02/05/getting-started-with-azure-kubernetes-service) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A streamlined onboarding guide outlining the core mechanics of building, deploying, and maintaining basic cluster topologies in AKS. Provides a solid foundation covering cluster creation parameters via Azure CLI, container registry linkage, and basic networking. Recommended for developers transitionining from local docker engines to managed cloud-native environments.
#### Operations

  - **(2024)** [techcommunity.microsoft.com: Leveraging Azure Copilot for Azure Kubernetes Services (AKS)](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/leveraging-azure-copilot-for-azure-kubernetes-services-aks/4212457) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Discusses integrating Microsoft Copilot generative AI models within the Azure Kubernetes Service management plane. Highlights AI-assisted troubleshooting workflows, automated diagnostics, YAML generation, and resource tuning suggestions. Represents the emerging state of artificial intelligence operations (AIOps) in cloud-native management.
#### Security (1)

  - **(2024)** [learn.microsoft.com: Deploy AKS and API Management with mTLS](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-mutual-certificates-for-clients) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation for implementing mutual TLS (mTLS) configurations between Azure API Management (APIM) and backend AKS services. Includes certificate exchange setups, ingress controller enforcement (such as NGINX), and identity validation processes. Necessary blueprinting for highly compliant systems such as open-banking and healthcare APIs.
  - **(2023)** [techcommunity.microsoft.com: Securing Windows workloads on Azure Kubernetes Service with Calico](https://techcommunity.microsoft.com/blog/containers/securing-windows-workloads-on-azure-kubernetes-service-with-calico/3815429) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This architectural guide details how to leverage Tigera Calico's CNI and policy engine to enforce advanced microsegmentation on Windows workloads within Azure Kubernetes Service (AKS). It addresses heterogeneous node pool configurations (Windows and Linux mixed architectures) and demonstrates how to apply consistent security policies across dual-OS workloads to meet strict enterprise isolation and compliance requirements.
### Google Kubernetes Engine GKE

#### Cost Optimization (4)

  - **(2021)** [cloud.google.com: Announcing Spot Pods for GKE Autopilot—save on fault tolerant workloads](https://cloud.google.com/blog/products/containers-kubernetes/announcing-spot-pods-for-gke-autopilot) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Spot Pods for GKE Autopilot, enabling cost reductions of up to 60-80% for fault-tolerant, stateless workloads and background microservices. Examines how Autopilot schedules, preempts, and relocates workloads based on Google's excess compute capacity without operator intervention.
#### DNS Optimization

  - **(2024)** [Setting up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed technical guide to configuring NodeLocal DNSCache on GKE clusters. By running a lightweight caching agent as a node-level DaemonSet, this pattern prevents connection track table exhaustion and significantly decreases DNS lookup latency for high-throughput microservices.
  - **(2024)** [Kubernetes Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#vpc_scope_dns) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical documentation for implementing Cloud DNS for GKE. Illustrates how integrating managed GCP Cloud DNS with GKE clusters removes the CPU/Memory overhead of running in-cluster CoreDNS (kube-dns) instances. Essential for highly-scaled microservices architectures prone to DNS query bottlenecking.
#### Evolution and History

  - **(2020)** [Looking ahead as GKE, the original managed Kubernetes, turns 5](https://cloud.google.com/blog/products/containers-kubernetes/5-ways-google-cloud-is-making-gke-the-best-place-to-run-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical piece reflecting on the five-year evolutionary path of GKE as the pioneer managed Kubernetes provider. Explores the development of multi-cluster mechanics, integrated security baselines, and automated upgrade routines. Valuable as context for evaluating current orchestrator capabilities.
#### FinOps

  - **(2022)** [cloud.google.com: Know more, spend less: how GKE cost optimization insights help you optimize Kubernetes](https://cloud.google.com/blog/products/containers-kubernetes/gke-cost-optimization-insights-now-ga) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines GKE's native cost optimization insights, which surface over-provisioned CPU/Memory metrics directly within the console. Guides platform architects on utilizing automated rightsizing recommendations to minimize container cost overruns while maintaining necessary performance profiles.
#### Industry Analysis

  - **(2021)** [techcrunch.com: Google Cloud puts its Kubernetes Engine on autopilot](https://techcrunch.com/2021/02/24/google-cloud-puts-its-kubernetes-engine-on-autopilot) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — TechCrunch's coverage of GKE Autopilot, highlighting its impact on managed container orchestration trends. Focuses on the trade-offs of restricting low-level node configurations in exchange for SLA-backed operations and optimized bin-packing. Evaluates the strategic TCO reductions of serverless-style Kubernetes models.
  - **(2021)** [zdnet.com: Google introduces GKE Autopilot for hands-off Kubernetes](https://www.zdnet.com/article/google-introduces-gke-autopilot-for-hands-off-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — ZDNet analysis of GKE Autopilot, detailing how the serverless operational paradigm mitigates day-2 engineering friction. Discusses how automated cluster provisioning, continuous hardening, and SLA integration allow software delivery teams to target product deployment over raw node configuration.
#### Ingress and Routing (1)

  - **(2022)** [Using new traffic control features in External HTTP(S) load balancer](https://cloud.google.com/blog/products/networking/how-to-use-new-traffic-control-features-in-cloud-load-balancing) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details advanced traffic engineering patterns utilizing Google Cloud external HTTP(S) Load Balancing. Outlines how GKE architects can configure header-based request redirection, traffic mirroring, and weight-based canary routes directly at the external ingress tier to construct robust microservices patterns.
#### Multi-Cluster Architectures

  - **(2022)** [cloud.google.com: How to do multi-cluster Kubernetes in the real world—one GKE shop’s approach](https://cloud.google.com/blog/products/containers-kubernetes/multi-cluster-kubernetes-with-gke-at-geotab) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A real-world engineering case study from Geotab detailing their approach to multi-cluster GKE administration. Addresses cross-region latency issues, regional failover strategies, and global DNS configurations, demonstrating how to maintain highly available microservices environments at scale.
#### Multi-Cluster Networking

  - **(2021)** [cloud.google.com: Discover and invoke services across clusters with GKE multi-cluster services](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-multi-cluster-services) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces GKE Multi-Cluster Services (MCS), allowing cross-cluster service discovery and load balancing using standard Kubernetes primitives. Enables seamless cross-cluster communication, simplifying geographic scaling, disaster recovery architectures, and multi-region microservice fabrics.
#### Observability (2)

  - **(2022)** [cloud.google.com: Introducing Kubernetes control plane metrics in GKE](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-control-plane-metrics-are-generally-available) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details how to configure GKE's native integration of control plane metrics into Google Cloud Monitoring. Surfacing etcd operations and API server transaction queues, this feature resolves a critical visibility gap for operators troubleshooting scheduling bottlenecks and control plane latency.
  - **(2020)** [codeburst.io: Google Kubernetes Engine Logging by Example](https://codeburst.io/google-kubernetes-engine-logging-by-example-df6946dcba6b) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates structured logging patterns using Google Cloud Logging (formerly Stackdriver) inside GKE. Guides developers on outputting logs in structured JSON formats to facilitate unified search queries, metrics extraction, and alert generation. While older, the foundational concepts of structured observability remain highly applicable.
#### Operational Tradeoffs

  - **(2021)** [thenewstack.io: Google’s New ‘Autopilot’ for Kubernetes](https://thenewstack.io/googles-new-autopilot-for-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical comparison contrasting GKE Standard and GKE Autopilot models. Outlines the security boundaries imposed by Autopilot (restricting root-level DaemonSets and direct SSH access) in exchange for hands-off resource optimization. Highly relevant for platform architects auditing cluster governance models.
#### Performance Scaling

  - **(2021)** [acloudguru.com: GKE ludicrous speed! GKE Image Streaming speeds up container starts](https://www.pluralsight.com/resources/blog/cloud/gke-ludicrous-speed-gke-image-streaming-speeds-up-container-starts) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores GKE Image Streaming, a performance feature that speeds up container startups by lazy-loading image layers over the network. By starting pods before the entire image is downloaded, this architecture accelerates auto-scaling and quickens recovery times from node failures.
#### Security and Compliance (1)

  - **(2024)** [==google/gke-policy-automation==](https://github.com/google/gke-policy-automation) <span class='md-tag md-tag--info'>⭐ 524</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A Google-maintained open-source tool designed to automate policy audits on GKE cluster setups using Open Policy Agent (OPA) Gatekeeper. This utility inspects cluster configuration dumps against best practices, helping security engineers secure their container footprints.
#### Security and IAM

  - **(2024)** [Fetches all Primitive and Predefined GCP IAM Roles](https://github.com/darkbitio/gcp-iam-role-permissions) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source security tool that parses and exports GCE IAM pre-defined and primitive role definitions. Helps platform security architects map precise least-privilege configurations when implementing Workload Identity bounds inside production GKE clusters.
#### Serverless Orchestration

  - **(2025)** [cloud.google.com: GKE Autopilot 🌟](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive official documentation for GKE Autopilot. Guides engineers through the platform's security boundaries, billing dimensions (vCPU, memory, storage), and workload restrictions (such as system capabilities and host namespaces). Serves as the primary reference guide for production deployments.
  - **(2021)** [Introducing GKE Autopilot: a revolution in managed Kubernetes 🌟](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-autopilot) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official launch publication outlining the engineering principles behind GKE Autopilot. Explains how Autopilot shifts operational responsibilities to Google SREs by managing underlying node infrastructure dynamically. Workload scaling is billed based on actual requested pod resources, implementing a secure, hands-off operational model.
#### Visual Guides

  - **(2021)** [youtube: GKE Autopilot - Fully Managed Kubernetes Service From Google 🌟](https://www.youtube.com/watch?v=Zztufl4mFQ4&feature=youtu.be) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual and practical video walkthrough demonstrating GKE Autopilot cluster generation, workload manifest adjustment, and basic operational validation. Useful for engineers seeking a fast introduction to serverless container deployment patterns.
### Microsoft AKS

#### Architecture Baseline

##### Secure Architecture

  - **(2023)** [docs.microsoft.com: Baseline architecture for an Azure Kubernetes Service (AKS) cluster 🌟](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official Azure Well-Architected Framework baseline architecture for establishing a highly secure, private, and resilient AKS cluster. Focuses on network isolation, hub-spoke topology, and enterprise integration.
#### Getting Started (1)

##### Core Concepts

  - **(2023)** [learn.microsoft.com: Introduction to Kubernetes on Azure](https://learn.microsoft.com/en-us/training/paths/intro-to-kubernetes-on-azure) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guided learning pathway introducing the core operational mechanics of Azure Kubernetes Service (AKS). Outlines control-plane abstractions, compute node orchestration, and Azure platform-native integrations.
#### Infrastructure as Code (2)

##### Template Generator

  - **(2023)** [azure.github.io/AKS-Construction 🌟](https://azure.github.io/AKS-Construction) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Interactive deployment engine for generating secure, enterprise-grade Infrastructure-as-Code templates for AKS. Supports Terraform, Bicep, and ARM formats tailored to strict corporate baseline requirements.
#### Lifecycle and Release Notes

##### Platform Changes

  - **(2024)** [Azure Updates AKS 🌟](https://azure.microsoft.com/en-us/updates/?query=AKS) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official real-time tracking feed for feature rollouts, API updates, region additions, and critical deprecation schedules affecting Azure Kubernetes Service.
#### Microservices Design (1)

##### Production Architecture

  - **(2023)** [docs.microsoft.com: Microservices architecture on Azure Kubernetes Service (AKS) 🌟](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural design guide detailing enterprise container patterns for deploying robust, scalable, and secure microservices architectures natively inside Azure Kubernetes Service.
#### Migration and Modernization

##### App Containerization

  - **(2021)** [techcommunity.microsoft.com: Containerize and migrate applications to AKS with the Azure Migrate’s new App Containerization tool](https://techcommunity.microsoft.com/blog/azuremigrationblog/containerize-and-migrate-applications-to-aks-with-the-azure-migrate%e2%80%99s-new-app-co/2178551) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Introduces Microsoft's built-in App Containerization tool to streamline migrating legacy ASP.NET and Java web servers into AKS-compatible containerized deployments.
#### Networking (3)

##### Azure CNI

  - **(2023)** [docs.microsoft.com: Configure Azure CNI networking in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — In-depth technical configuration specifications for implementing the high-performance Azure CNI plugin on AKS clusters. Analyzes structural routing paths, IP allocation dynamics, and integration configurations.
##### Kubenet Configuration

  - **(2023)** [docs.microsoft.com: Use kubenet networking with your own IP address ranges in Azure Kubernetes Service (AKS) 🌟](https://learn.microsoft.com/en-us/azure/aks/configure-kubenet) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive configuration guide describing how to implement Kubenet networking in AKS using optimized, restricted IP boundaries. Balances IP consumption limitations with operational simplicity.
#### Production Checklist

##### Best Practices (3)

  - **(2023)** [the-aks-checklist.com: The Azure Kubernetes Service Checklist 🌟🌟🌟](https://www.the-aks-checklist.com) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive diagnostic tool assisting operators in preparing AKS environments for production. Covers critical checkboxes across scalability, network layouts, security configurations, and cost efficiency.
#### Runtime Environments

##### Windows Containers

  - **(2020)** [nillsf.com: Running Windows containers on the Azure Kubernetes Service (AKS)](https://nillsf.com/index.php/2020/11/17/running-windows-containers-on-the-azure-kubernetes-service-aks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Operational overview detailing how to build, deploy, scale, and manage traditional Windows Server workload containers securely on dedicated Windows node pools in AKS.
#### Scheduling and Taints

##### Compute Node Pools

  - **(2022)** [trstringer.com: Run Kubernetes Pods on Specific VM Types in AKS](https://trstringer.com/run-kubernetes-pods-on-vm-types) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores structural scheduling patterns inside AKS to assign dedicated workloads onto specific VM sizes using node selectors, taints, tolerations, and node affinity rules.
#### Security and Identity

##### Entra ID Auth

  - **(2023)** [docs.microsoft.com: AKS-managed Azure Active Directory integration](https://learn.microsoft.com/en-us/azure/aks/entra-id-control-plane-authentication) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides engineers in utilizing integrated Microsoft Entra ID (formerly Azure AD) to control access to AKS cluster operations via RBAC mappings and active identity directory validation.
##### Pod Identity Evolution

  - **(2021)** [github.com: AKS: Use AAD identity for pods and make your SecOps happy](https://github.com/dfrappart/articles/blob/master/podidentityjourney.md) <span class='md-tag md-tag--info'>⭐ 6</span> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Journal exploring Azure AD Pod Identity to authorize pods. Note: While historically significant, modern live grounding indicates this pattern has been succeeded by Microsoft Entra Workload Identity.
#### Storage (2)

##### StatefulSet Volume Scaling

  - **(2022)** [adamrushuk.github.io: Increasing the volumeClaimTemplates Disk Size in a Statefulset on AKS](https://adamrushuk.github.io/increasing-the-volumeclaimtemplates-disk-size-in-a-statefulset-on-aks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Addresses technical hurdles and step-by-step procedures when attempting to live-resize Persistent Volumes linked to stateful applications orchestrated via StatefulSets inside AKS.
## Cloud-Native Infrastructure

### Cluster Provisioning (2)

#### High Availability (2)

  - **(2021)** [itnext.io: Adding Master Nodes to Achieve HA: One of the Best Practices for Using KubeKey](https://itnext.io/adding-master-nodes-to-achieve-ha-one-of-the-best-practices-for-using-kubekey-6207e94b0bdd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the deployment patterns needed to scale control-plane nodes from single instances to high-availability multi-master architectures using KubeKey. It covers load-balancer integrations, internal ETCD cluster configurations, and control-plane state replication. (Live Grounding: Provides practical blueprints for production-grade self-managed control plane environments).
#### KubeKey

  - **(2025)** [**kubekey**](https://github.com/kubesphere/kubekey) <span class='md-tag md-tag--info'>⭐ 2821</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A Go-based command-line utility engineered to rapidly install, configure, and upgrade Kubernetes clusters, KubeSphere components, and runtime layers (containerd, Docker) on bare-metal and cloud environments. It highly excels in air-gapped, offline installations using custom artifact packages. (Live Grounding: KubeKey remains a highly-rated installer alternative to Kubeadm, especially popular in hybrid/on-prem environments requiring deterministic runtime setups).
  - **(2021)** [kubesphere.io: Install Kubernetes 1.22 and containerd the Easy Way with kubekey](https://kubesphere.io/blogs/install-kubernetes-containerd) <span class='md-tag md-tag--warning'>[GO/YAML CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Outlines a streamlined procedural approach to installing Kubernetes 1.22 and containerd using the KubeKey engine. The guide emphasizes the migration away from Docker shim and configures high-performance runtime options using bare-metal architecture targets. (Live Grounding: Although v1.22 is legacy by 2026 standards, the architectural concepts of containerd orchestration and bare-metal bootstrapping via KubeKey remain highly instructional).
  - **(2021)** [kubesphere.io: Scaling a Kubernetes Cluster: One of the Best Practices for Using KubeKey](https://kubesphere.io/blogs/scale-kubernetes-cluster-using-kubekey) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A technical guide demonstrating how to horizontally scale existing Kubernetes compute capacities using KubeKey execution manifests. Focuses on declarative modifications of cluster-configuration files to dynamically append new worker nodes without service disruptions. (Live Grounding: Vital operations reference for cluster administrators managing hardware expansions within hybrid/private clouds).
### Managed Kubernetes

#### Azure AKS

  - **(2025)** [youtube: The AKS Community](https://www.youtube.com/@theakscommunity) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated developer and operator community resource focusing on Azure Kubernetes Service (AKS). Tracks the evolution of enterprise-ready features, including node autoscale profiles, azure-cni overlays, Workload Identity, and cost optimization practices. (Live Grounding: Serves as an invaluable hub for tracking live updates directly from Microsoft engineers).
## Cluster Architecture

### Sizing

#### Node Allocatable

  - **(2023)** [learnk8s.io: Allocatable memory and CPU in Kubernetes Nodes](https://learnkube.com/allocatable-resources) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demystifies how Kubernetes computes physical allocatable resources. Deeply details the underlying formulas for `kube-reserved`, `system-reserved`, and eviction thresholds to ensure cluster stability under heavy workloads.
## Container Platforms

### Enterprise Platforms

#### Cluster API

  - **(2022)** [giantswarm.io:](https://www.giantswarm.io/blog/turtles-all-the-way-down-are-still-just-turtles-giant-swarm) <span class='md-tag md-tag--warning'>[GO/YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — An in-depth post detailing Giant Swarm's operational adoption of Cluster API (CAPI) for provisioning 'clusters within clusters.' It breaks down the philosophical and technical paradigms of declarative multi-cluster orchestration where management planes treat tenant clusters as Kubernetes resources. (Live Grounding: Illustrates the robust shift away from legacy custom provisioning scripts toward cloud-native standard CAPI specifications).
#### KubeSphere

  - **(2026)** [kubesphere.io](https://kubesphere.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — KubeSphere is a distributed, multi-tenant enterprise container platform built on top of Kubernetes. It provides an intuitive GUI dashboard for managing multi-cloud container orchestration, DevOps pipelines (Jenkins-based), service meshes (Istio), observability, and microservice governance. (Live Grounding: Actively developed in 2026, offering a complete, modular, cloud-agnostic platform alternative to OpenShift).
  - **(2020)** [itnext.io: KubeSphere: A New Pluggable Kubernetes Application Management Platform](https://itnext.io/kubesphere-a-new-pluggable-kubernetes-application-management-platform-bf078b9f3330) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the modular and pluggable architecture of KubeSphere, showing how enterprises can customize their deployments by enabling or disabling components like DevOps, Service Mesh, and Logging/Monitoring. Discusses native application lifecycle management integrations. (Live Grounding: Underlines KubeSphere's strategic market position as a flexible, lower-overhead alternative to Red Hat OpenShift).
#### Managed Kubernetes (1)

  - **(2026)** [Giant Swarm](https://www.giantswarm.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Giant Swarm is an enterprise-tier fully managed Kubernetes platform that emphasizes cluster lifecycle management across multi-cloud environments (AWS, Azure) and bare-metal setups. Known for utilizing the Cluster API (CAPI) pattern to automate cluster lifecycle management natively. (Live Grounding: Solidly positioned as a premium provider of GitOps-driven, multi-tenant container orchestration architectures in 2026).
## Delivery and CICD

### Application Packaging

#### Draft and Acorn

  - **(2023)** [medium.com/@pauldotyu: Effortlessly Deploy to AKS with Open Source Tools Draft and Acorn](https://medium.com/@pauldotyu/app-to-aks-with-draft-and-acorn-2d25f19649b7) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Focuses on simplifying development workflows on AKS using Draft and Acorn. Streamlines container generation and cluster deployments. Live grounding note: Acorn changed operations in early 2024, emphasizing legacy community-tool status.
### Continuous Deployment

#### Azure Pipelines

  - **(2023)** [azuredevopslabs.com: Deploying a multi-container application to Azure Kubernetes Services](https://azuredevopslabs.com/labs/vstsextend/kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An interactive, practical lab illustrating the step-by-step setup of continuous delivery pipelines targeting AKS using Azure DevOps. Covers container builds, ACR image pushes, and multi-stage YAML pipeline deployment structures.
## Developer Experience

### Inner Loop Development

#### Local Tooling

  - **(2023)** [==Azure/Draft 🌟==](https://github.com/Azure/draft) <span class='md-tag md-tag--info'>⭐ 642</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Azure Draft simplifies early-stage developer onboarding onto Kubernetes. By scanning source code directories, it automatically generates containerization assets including Dockerfiles, Kubernetes manifests, Helm charts, and deployment workflows.
## Development Tools

### Storage (3)

#### Volume Synchronization

  - **(2026)** [==github.com/rebataur/djkube==](https://github.com/rebataur/fskube) <span class='md-tag md-tag--info'>⭐ 27</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A lightweight, community-driven development aid designed to bridge local filesystems with Kubernetes volumes. Live Grounding indicates the project has had minimal recent activity, classifying it as a legacy utility. It may serve as a historical reference implementation for simple synchronization mechanisms.
## FinOps and Cloud Cost

### AWS Optimization

#### EKS Log Optimization

  - **(2023)** [**aws.amazon.com: Understanding and Cost Optimizing Amazon EKS Control Plane Logs**](https://aws.amazon.com/blogs/containers/understanding-and-cost-optimizing-amazon-eks-control-plane-logs) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Analyzes the high CloudWatch cost challenges generated by Amazon EKS control plane logs (API server, authenticator, audit, scheduler). Demonstrates how to configure fluent-bit to filter and route only essential telemetry records to cheap storage.
### Kubernetes FinOps

#### Cost Management

  - **(2023)** [==infoworld.com: Kubernetes cost management for the real world==](https://www.infoworld.com/article/2338428/kubernetes-cost-management-for-the-real-world.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A deep dive into the challenges of multi-tenant Kubernetes cost attribution across dynamic namespaces. Contrasts raw hyper-scaler billing records against granular container resource consumption metrics, detailing how Kubecost and OpenCost establish accurate, real-world chargeback frameworks.
## Financial Operations

### Cost Optimization (5)

#### Node Allocation

  - **(2021)** [zartis.com: How To Save A Fortune On Azure Kubernetes Service](https://www.zartis.com/minimizing-costs-aks) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details structural cost optimization methods for AKS deployment. Discusses right-sizing node configurations, deploying Azure Spot instances for non-critical environments, and configuring cluster autoscalers. Grounding confirms these strategies are essential in architectural cost-governance pipelines.
## Infrastructure

### Enterprise Backup

#### Cloud-Native Integration

  - **(2021)** [**cloud.google.com: Announcing Backup for GKE: the easiest way to protect GKE workloads**](https://cloud.google.com/blog/products/storage-data-transfer/google-cloud-launches-backups-for-gke) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An announcement introducing Backup for GKE, a fully-managed Google Cloud service for GKE environments. Operates via the GCP API control plane to restore configurations and storage elements natively.
### Hybrid and On-Premises

#### Azure Stack Hub

  - **(2021)** [techcommunity.microsoft.com: Azure Kubernetes Service and Azure Container Registry Service on Azure Stack Hub](https://techcommunity.microsoft.com/blog/azurestackblog/azure-kubernetes-service-and-azure-container-registry-service-on-azure-stack-hub/3075932) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines deploying managed AKS and container registries (ACR) onto Azure Stack Hub, which acts as a hybrid infrastructure setup. Solves data sovereignty, regulatory compliance, and low-latency challenges for edge deployments inside closed datacenters.
### Ingress and Routing (2)

#### Application Gateway AGIC

  - **(2022)** [returngis.net: Configurar más de un Application Gateway con AGIC para AKS](https://www.returngis.net/2022/05/configurar-mas-de-un-application-gateway-con-agic-para-aks) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Written in Spanish, this technical guide explains how to control multiple Azure Application Gateways through a single AGIC controller inside AKS. Explains resource routing partitions between internal microservices and public endpoints.
  - **(2020)** [itnext.io: Kubernetes Ingress on Azure using the Application Gateway](https://itnext.io/kubernetes-ingress-on-azure-using-the-application-gateway-2779b647deb5) <span class='md-tag md-tag--warning'>[YAML/TERRAFORM CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes configuring the Application Gateway Ingress Controller (AGIC) to leverage Azure's Layer 7 load balancer inside AKS clusters. Outlines integrating native Web Application Firewall (WAF) services and avoiding extra routing hops. Promotes scalable network architectures for modern APIs.
#### Dynamic DNS

  - **(2022)** [dev.to/javiermarasco: HTTPs with Ingress controller, cert-manager and DuckDNS (in AKS/Kubernetes)](https://dev.to/javiermarasco/https-with-ingress-controller-cert-manager-and-duckdns-in-akskubernetes-2jd1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents a dynamic DNS development environment setup using cert-manager, NGINX ingress, and DuckDNS on AKS clusters. Helps development teams quickly wire secure, externally accessible TLS endpoints without needing official domain registrations.
#### ExternalDNS

  - **(2023)** [techcommunity.microsoft.com: Kubernetes External DNS for Azure DNS & AKS](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/kubernetes-external-dns-for-azure-dns--aks/3809393) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines configuring ExternalDNS inside an AKS cluster to dynamically sync Kubernetes Ingress resources with Azure DNS zones. Avoids manual DNS configuration, automating resource and IP updates on target domain records.
#### Hybrid Ingress Architecture

  - **(2021)** [returngis.net: Azure Application Gateway con WAF y wildcard + Nginx Controller para AKS](https://www.returngis.net/2021/11/azure-application-gateway-con-waf-y-wildcard-nginx-controller-para-aks) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Spanish-language architecture guide demonstrating a hybrid ingress design: placing an Azure Application Gateway (with WAF enabled) in front of an in-cluster NGINX ingress controller. Solves wildcard SSL setups and advanced ingress rules within AKS.
#### TLS Ingress Controller

  - **(2020)** [docs.microsoft.com: Create an HTTPS ingress controller on Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/previous-versions/azure/aks/ingress-tls) <span class='md-tag md-tag--warning'>[YAML/BASH CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A legacy Microsoft technical manual outlining the step-by-step deployment of an NGINX ingress controller with cert-manager on AKS. Curators highlight its historical value in configuring dynamic TLS certificates via Let's Encrypt. Live grounding shows this is marked as a legacy/previous version doc, as engineering teams in 2026 favor native Application Gateway Ingress Controller (AGIC) or native Istio integrations.
### Networking and CNI

#### Azure CNI Cilium

  - **(2022)** [isovalent.com: Announcing Azure CNI Powered by Cilium](https://isovalent.com/blog/post/azure-cni-cilium) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Isovalent's technical summary showcasing Azure CNI powered by Cilium integration. This architecture combines Azure's high-performance native routing fabrics with the advanced, secure eBPF-driven networking layer of Cilium. Represents the modern standard for fast AKS networking in 2026.
#### Azure CNI Overlay

  - **(2023)** [azure.microsoft.com: Announcing the general availability of Azure CNI Overlay in Azure Kubernetes Service](https://azure.microsoft.com/en-us/blog/announcing-the-general-availability-of-azure-cni-overlay-in-azure-kubernetes-service) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes Microsoft's GA release of Azure CNI Overlay in AKS. This network model decouples Pod IPs from VM subnets, mitigating private IP depletion issues and enabling clusters to scale to thousands of nodes without complex virtual network refactoring.
#### BYO CNI

  - **(2022)** [pixelrobots.co.uk: Bring your own Container Network Interface (CNI) plugin with Azure Kubernetes Service (AKS) (PREVIEW)](https://pixelrobots.co.uk/2022/04/bring-your-own-container-network-interface-cni-plugin-with-azure-kubernetes-service-aks-preview) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines utilizing the Bring Your Own CNI (BYO CNI) preview option in AKS. Allows engineering teams to manage and run their own custom CNI platforms (such as custom Cilium structures) while still leveraging the managed control plane benefits of AKS.
#### Calico eBPF

  - **(2021)** [thenewstack.io: Turbocharging AKS Networking with Calico eBPF](https://thenewstack.io/turbocharging-aks-networking-with-calico-ebpf) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the performance enhancements derived from running Calico's eBPF data plane over AKS cluster topologies. Discusses how bypassing traditional iptables routing overhead reduces connection latency and CPU usage. It remains a relevant comparative benchmark for high-performance networks.
  - **(2021)** [tigera.io: Turbocharging AKS networking with Calico eBPF](https://www.tigera.io/blog/turbocharging-aks-networking-with-calico-ebpf) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official Tigera blog post covering the implementation steps for deploying the Calico eBPF data plane on AKS networks. Shows direct performance comparison over standard networking schemes. Highlights resource savings, security enforcement, and high-speed data planes.
#### Kubenet vs Azure CNI

  - **(2022)** [medium.com/@vamsi.lakshman: Overview of Azure Kubernetes Services Networking Models](https://medium.com/@vamsi.lakshman/overview-of-azure-kubernetes-services-networking-models-e3ca0591aebe) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a comprehensive architectural overview contrasting AKS's native CNI models: Kubenet versus Azure CNI. Analyzes the trade-offs of IP space consumption, routing tables, and overall performance dynamics across large clusters.
#### WireGuard Encryption

  - **(2021)** [tigera.io: Calico WireGuard support with Azure CNI](https://www.tigera.io/blog/calico-wireguard-support-with-azure-cni) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines configuring Calico WireGuard encryption overlaying Azure CNI networks. Details setting up highly secure node-to-node transport layer encryption with minimal CPU overhead. Grounding points to this as an excellent alternative to heavy IPsec deployments.
### Node Pools

#### Windows Containers (1)

  - **(2022)** [dev.to: Getting started with Windows Containers on Azure Kubernetes Service](https://dev.to/rdvansloten/getting-started-with-windows-containers-on-azure-kubernetes-service-46ce) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A fundamental playbook illustrating setup tasks for hosting Windows Server containers inside AKS node pools. Explains common pitfalls including licensing, customized networking modes, and configuring dual-OS deployments alongside Linux nodes.
### Provisioning and IaC

#### ARM Templates

  - **(2020)** [docs.cloudblue.com: Deploying an AKS Cluster with Custom IP Ranges (ARM template)](https://docs.cloudblue.com/cbc/20.5/premium/content/Deployment-of-Product-to-Azure-Cloud-Guide/Deploying-AKS-Cluster-with-Custom-IP-Ranges.htm) <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the construction of ARM templates to deploy AKS clusters containing custom network IP range allocations. Ensures smooth compliance within pre-defined enterprise internal network spaces. Grounding shows ARM is stable, although Bicep and Terraform are dominant in 2026.
#### AWS CDK and Multicluster

  - **(2022)** [Using CDK to perform continuous deployments in multi-region Kubernetes environments](https://aws.amazon.com/blogs/containers/using-cdk-to-perform-continuous-deployments-in-multi-region-kubernetes-environments) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the use of AWS Cloud Development Kit (CDK) to model continuous delivery systems across multi-region Kubernetes deployments. Highly relevant for cloud engineers designing hybrid-cloud architectures that span AKS and EKS infrastructure.
### Storage Systems

#### Private Endpoints

  - **(2021)** [carlos.mendible.com: AKS: Persistent Volume Claim with an Azure File Storage protected with a Private Endpoint](https://carlos.mendible.com/2021/08/02/aks-persistent-volume-claim-with-an-azure-file-storage-protected-with-a-private-endpoint) <span class='md-tag md-tag--warning'>[YAML/TERRAFORM CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines configuring a Persistent Volume Claim (PVC) using Azure Files storage secured with a Private Endpoint in AKS. Prevents the storage accounts from being exposed to the public internet. Grounding confirms this is a critical enterprise pattern for storage layer hardening.
## Infrastructure as Code and CI-CD

### CI-CD Pipelines

#### GitHub Actions

##### Oracle Cloud Infrastructure

  - **(2021)** [arnoldgalovics.com: GitHub Actions CI/CD For Oracle Cloud Kubernetes](https://arnoldgalovics.com/github-actions-oracle-cloud-kubernetes) <span class='md-tag md-tag--warning'>[YAML/SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed technical walkthrough showcasing the implementation of automated deployment pipelines using GitHub Actions to target Oracle Cloud Infrastructure Container Engine for Kubernetes (OKE). It delineates secure OCI API authentication configurations, container image construction, and rollout orchestrations. (Live Grounding: Represents a standard, practical approach to OKE deployments using runners, contrasting with traditional enterprise Jenkins setups).
#### KubeSphere (1)

##### Jenkins

  - **(2022)** [youtube: Create a Jenkins Pipeline on Kubernetes with CI/CD Pipeline Template in KubeSphere](https://www.youtube.com/watch?v=MU5LdM83x9s&t=40s&ab_channel=KubeSphere) <span class='md-tag md-tag--warning'>[GROOVY/YAML CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A visual demonstration detailing the creation of declarative Jenkins pipelines within the KubeSphere platform interface. Covers pipeline templates, integrated credential stores, and multi-stage container build-to-deploy workflows inside Kubernetes namespaces. (Live Grounding: Demonstrates how KubeSphere bridges legacy Jenkins pipelines with cloud-native execution runners).
## Multi-Cloud Management

### Platform Engineering (1)

#### Tooling Comparison

  - **(2021)** [Compare tools for multi-cloud Kubernetes management 🌟](https://www.techtarget.com/searchcloudcomputing/tip/Compare-tools-for-multi-cloud-Kubernetes-management) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Synthesizes and contrasts several enterprise-grade multi-cloud Kubernetes management suites including Red Hat OpenShift, Rancher, Platform9, and Terraform. Highlights the design trade-offs between hypervisor-style centralized management interfaces and modular GitOps delivery systems. (Live Grounding: While some listed tools like StackPointCloud are defunct or archived, the architectural comparison criteria remains critical for multi-cluster evaluations in 2026).
## Observability (3)

### Telemetry

#### Azure Monitoring

  - **(2022)** [grafana.com: Scrape Azure metrics and monitor AKS using Grafana Agent 🌟](https://grafana.com/blog/scrape-azure-metrics-and-monitor-aks-using-grafana-agent) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A telemetry extraction guide focused on deploying Grafana Agent inside AKS to scrape and forward metrics directly to Grafana Cloud. Avoids expensive, proprietary log-forwarding configurations and maintains unified telemetry visualization dashboards.
## Operations and Troubleshooting

### Diagnostic Analysis

#### Core Dumps

  - **(2020)** [blog.nillsf.com: Customize core dump in Azure Kubernetes](https://blog.nillsf.com/index.php/2020/12/06/customize-core-dump-in-azure-kubernetes) <span class='md-tag md-tag--warning'>[BASH/YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes advanced kernel-level customizations required to capture core dumps from Linux containers running on AKS. Focuses on configuring host path directories, container filesystem capabilities, and kernel variables. Grounding shows this is vital for diagnostic debugging in low-level runtime environments (C++/.NET) where standard logs fail during sudden container restarts.
#### Windows Packet Capture

  - **(2020)** [github.com/OvidiuBorlean/kubectl-windumps](https://github.com/OvidiuBorlean/kubectl-windumps) <span class='md-tag md-tag--info'>⭐ 7</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A legacy kubectl command-line utility facilitating TCP packet captures directly on Windows Server nodes within AKS clusters. Live grounding shows the project has been inactive for several years, yet it serves as a valuable conceptual reference for troubleshooting deep network issues.
#### Windows RDP Troubleshooting

  - **(2023)** [learn.microsoft.com: Connect with RDP to Azure Kubernetes Service (AKS) cluster Windows Server nodes for maintenance or troubleshooting](https://learn.microsoft.com/en-us/azure/aks/rdp) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the official configuration workflows to safely establish RDP (Remote Desktop Protocol) connections into AKS Windows Server nodes. Facilitates deep system-level maintenance, networking diagnostics, and container execution debugging.
### Incident Response

#### Disaster Recovery

  - **(2022)** [community.ops.io: One day I woke up to a crashed AKS cluster and this is what I did to get it back to life](https://community.ops.io/javi_labs/one-day-wake-up-to-a-crashed-aks-cluster-and-this-is-what-i-did-to-get-it-back-to-life-1592) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An educational post-mortem detailing disaster recovery of a critically degraded AKS cluster. Highlights issues with custom DNS resolution, routing, and dynamic debugging tools. Serves as a great diagnostic checklist for production failures.
### Observability (4)

#### Prometheus and Grafana

  - **(2022)** [dev.to/thenjdevopsguy: Monitoring AKS With Prometheus and Grafana 🌟](https://dev.to/thenjdevopsguy/monitoring-aks-with-prometheus-and-grafana-9o8) <span class='md-tag md-tag--warning'>[YAML/HELM CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on manual demonstrating the setup of Prometheus and Grafana on AKS using Helm charts. Details the construction of monitoring pipelines, collection of custom performance metrics, and configuration of alert conditions.
### Resource Management

#### Node Deallocation

  - **(2022)** [returngis.net: Desescalar nodos de AKS apagando las máquinas en lugar de eliminarlas](https://www.returngis.net/2022/04/desescalar-nodos-de-aks-apagando-las-maquinas-en-lugar-de-eliminarlas) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This technical Spanish article describes an alternate cost-savings scaling mechanism in AKS. Suggests stopping/deallocating underlying node virtual machines inside scale sets instead of deleting them. Grounding notes this retains local system disk caches for fast restart times.
#### Node Pools Scaling

  - **(2022)** [docs.microsoft.com: Start and stop an Azure Kubernetes Service (AKS) node pool 🌟](https://learn.microsoft.com/en-us/azure/aks/start-stop-nodepools) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official Microsoft technical guide documenting native start/stop capabilities inside AKS user node pools. Simplifies operational management by shutting down scaling instances to minimize computing costs during inactive schedules.
## Orchestration

### AKS

#### Tutorials

  - **(2022)** [build5nines.com: Terraform: Create an AKS Cluster 🌟](https://build5nines.com/terraform-create-an-aks-cluster) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step practical guide detailing the construction of an AKS cluster using Terraform. Walks through basic variables, resource groups, virtual networks, and node configuration blocks.
### Azure Compute

#### AKS and ACI

  - **(2022)** [k21academy.com: Azure Kubernetes Service & Azure Container Instances For Beginners 🌟](https://k21academy.com/azure-cloud/azure-container-instances-and-kubernetes-service) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory training reference explaining Azure Kubernetes Service (AKS) and Azure Container Instances (ACI). Describes virtual node orchestration patterns to dynamically offload execution spikes from AKS onto ACI serverless compute.
### Azure Networking

#### AKS VNET Integration

  - **(2021)** [azurecloudai.blog: Deploy Azure Kubernetes Service (AKS) to a preexisting VNET](https://azurecloudai.blog/verify.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical guide outlining the architectural parameters needed to deploy Azure Kubernetes Service (AKS) within a custom, pre-existing Virtual Network (VNET). Addresses CIDR constraints, subnet delegation, and Azure CNI configurations.
### Data Protection

#### AKS Backup

  - **(2022)** [azure.microsoft.com: Private preview: Azure Kubernetes Service (AKS) Backup 🌟](https://azure.microsoft.com/en-us/updates?id=private-preview-aks-backup) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement details for Azure Kubernetes Service (AKS) Backup. Highlights native recovery features for stateful PVs and configuration states. Note: Now fully GA and enterprise-stable, this backup protocol integrates securely with Azure Backup Center.
### Kubernetes (1)

#### Managed Kubernetes Comparison

  - **(2021)** [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.io/blog/eks-vs-gke-vs-aks-jan2021) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A multi-dimensional comparison of the three primary managed Kubernetes services: AWS EKS, Google GKE, and Azure AKS. Weighs crucial metrics including control plane management fees, SLA guarantees, automated master scaling, and IAM-to-K8s role bindings.
### Kubernetes Security

#### EKS Secrets KMS

  - **(2021)** [devoriales.com: AWS EKS Secret Encryption: Securing Your EKS Secrets At Rest with AWS KMS](https://devoriales.com/aws-eks-secret-encryption-securing-your-eks-secrets-at-rest-with-aws-kms) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A security hardening guide detailing the setup of envelope encryption for Kubernetes Secrets within AWS EKS using Key Management Service (KMS) integrations. Crucial for complying with enterprise-grade data-at-rest protection standards.
## Performance and Scale

### Container Runtimes

#### Image Pull Optimization

  - **(2023)** [danielstechblog.io: Mitigating slow container image pulls on Azure Kubernetes Service](https://www.danielstechblog.io/mitigating-slow-container-image-pulls-on-azure-kubernetes-service) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details concrete strategies to accelerate slow container image pull durations on AKS. Discusses configuring Azure Container Registry (ACR) replica caches, optimizing network speeds, and tuning persistent storage configs.
### Resource Management (1)

#### LimitRanges

  - **(2021)** [itnext.io: AKS Performance: Limit Ranges](https://itnext.io/aks-performance-limit-ranges-8e18cbebe351) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on utilizing Kubernetes LimitRanges inside AKS to enforce resource quotas on CPU and memory usage. Explains how implementing default limits mitigates raw 'noisy neighbor' resource starvation. This is a foundational practice for sustaining stability in multi-tenant environments.
## Platform Engineering (2)

### CICD and Delivery

#### Developer Experience (1)

  - **(2023)** [youtube: Day -25 | No Dockerfile, No K8s Manifests | Setup CI/CD in 5 minutes for any programming language](https://www.youtube.com/watch?v=io_yBU7vhIo) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates rapid deployment flows to Kubernetes bypassing standard manual Dockerfile and YAML manifest configurations. Showcases automated scaffolding utilities like Draft and Cloud Native Buildpacks. Targeted at reducing onboarding friction for software developers moving applications to production orchestrators.
#### GitHub Actions (1)

  - **(2023)** [insights.project-a.com: Using GitHub Actions to deploy to Kubernetes in GKE 🌟](https://www.project-a.vc/perspectives) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical roadmap for setting up secure Continuous Delivery pipelines to GKE using GitHub Actions. Specifically covers passwordless identity validation utilizing GCP Workload Identity Federation (WIF) to eliminate long-lived GCP service account JSON keys. Walks through Docker builds, GCR/GAR pushes, and Helm deployments.
### Developer Experience (2)

#### Legacy Scaffolding

  - **(2022)** [blog.baeke.info: Trying out Draft 2 on AKS](https://baeke.info/2022/06/02/trying-out-draft-2-on-aks) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An early evaluation testing out the Draft v2 workflow within AKS environments. Evaluates standard dev loops and notes architectural changes between initial Draft implementations and subsequent buildpack-driven tools. Modern architects should target standard buildpacks and OCI artifacts over older Draft versions.
### GitOps (1)

#### Declarative Infrastructure

  - **(2021)** [seroter.com: Using the new Google Cloud Config Controller to provision and manage cloud services via the Kubernetes Resource Model](https://seroter.com/2021/08/18/using-the-new-google-cloud-config-controller-to-provision-and-manage-cloud-services-via-the-kubernetes-resource-model) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces the Google Cloud Config Controller, highlighting its use of the Kubernetes Resource Model (KRM) to declare and govern external GCP services. Allows platform teams to enforce stateful GitOps practices, treating cloud resources (like databases and networking) identical to standard Kubernetes manifests.
## Resilience

### Chaos Engineering (1)

#### Cloud Architecture

  - **(2021)** [Chaos engineering on Amazon EKS using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/devops/chaos-engineering-on-amazon-eks-using-aws-fault-injection-simulator) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical walkthrough demonstrating how to orchestrate chaos experiments on Amazon EKS using AWS Fault Injection Simulator (FIS). Highlights configuring managed cluster actions to trigger node terminations, API failures, and container termination within isolated namespaces.
## Security (2)

### Cloud Security

#### EKS Hardening

  - **(2024)** [Amazon EKS Best Practices Guide for Security 🌟](https://aws.github.io/aws-eks-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The definitive enterprise guide for hardening EKS clusters against cloud-native threats. It covers network segregation, IAM roles for service accounts (IRSA), secrets encryption, and runtime defense. This is a foundational checklist for any platform engineering team running on AWS.
## Security and Governance

### Access and Identity

#### Azure Key Vault

  - **(2023)** [community.ops.io: Configuring AKS to read secrets and certificates from Azure KeyVaults](https://community.ops.io/javi_labs/configuring-aks-to-read-secrets-and-certificates-from-azure-keyvaults-17o1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical reference manual demonstrating integration patterns using Secrets Store CSI Driver inside AKS. Focuses on dynamically injecting certificates, keys, and operational credentials from Azure Key Vault into container workloads.
  - **(2022)** [dev.to: Access Secrets in AKV using Managed identities for AKS 🌟](https://dev.to/vivekanandrapaka/access-secrets-from-akv-using-managed-identities-for-aks-91p) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Shows how to retrieve and access secrets securely within AKS workloads using Managed Identities and Azure Key Vault CSI Provider. Avoids persisting plaintext credentials in cluster definitions, mounting secrets as secure volumes instead.
#### OAuth2 Proxy

  - **(2022)** [kristhecodingunicorn.com: Setting Up OAuth 2.0 Authentication for Applications in AKS With NGINX and OAuth2 Proxy 🌟🌟](https://www.kristhecodingunicorn.com/post/k8s_nginx_oauth) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates how to secure web applications running on AKS by configuring an NGINX Ingress controller alongside OAuth2 Proxy. Outlines setup patterns for integrating external identity providers (OIDC) to protect internal APIs and microservices.
  - **(2022)** [kristhecodingunicorn.com: Setting Up OAuth 2.0 Authentication for Applications in AKS With NGINX and OAuth2 Proxy](https://www.kristhecodingunicorn.com/post/aks-oauth2-proxy-with-nginx-ingress-controller) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides detailed YAML deployment specs for running OAuth2 Proxy alongside NGINX on AKS. Demonstrates configuring ingress annotations and token validation loops, creating a robust baseline for securing production routes.
#### Workload Identity

  - **(2022)** [dev.to: Implement Azure AD Workload Identity on AKS with terraform](https://dev.to/maxx_don/implement-azure-ad-workload-identity-on-aks-with-terraform-3oho) <span class='md-tag md-tag--warning'>[TERRAFORM CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed playbook implementing Azure AD Workload Identity on AKS utilizing Terraform templates. Eliminates static secrets by mapping Azure Managed Identities with Kubernetes Service Accounts via federated OIDC token exchanges.
  - **(2022)** [blog.baeke.info: AKS Workload Identity Revisited](https://baeke.info/2022/11/24/aks-workload-identity-revisited) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A deep-dive analyzing Azure AD Workload Identity mechanics. Compares this modern OIDC token-exchange flow against legacy pod identities. Essential reading for secure application migrations requiring direct integration with Azure Cloud resources.
### Cluster Security

#### Multi-Tenancy Isolation

  - **(2022)** [docs.microsoft.com: Best practices for cluster isolation in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-cluster-isolation) <span class='md-tag md-tag--warning'>[YAML/MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides official architectural best practices regarding logical and physical multi-tenant isolation in AKS. Details utilizing network policies, namespaces, and Kubernetes RBAC. A crucial resource for enterprise operators planning multi-team cluster sharing models.
### Microservices Security

#### Pod Security and Identities

  - **(2020)** [medium: Secure your Microservices on AKS — Part 1 🌟](https://itnext.io/running-your-microservices-securely-on-aks-417a110b2e76) <span class='md-tag md-tag--warning'>[TERRAFORM/YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth security architecture guide covering secure microservices deployment on AKS. Leverages Azure Active Directory (AAD) Pod Identity (and modern Workload Identity shifts) along with network security policies. Details methods to restrict pod-to-pod communications, configure secret vaults, and enforce security baselines at the runtime layer.
### Network Security

#### Network Isolation

  - **(2021)** [itnext.io: Network Isolated AKS — Part 1: Controlling network traffic](https://itnext.io/network-isolated-aks-part-1-controlling-network-traffic-2cd0e045352d) <span class='md-tag md-tag--warning'>[TERRAFORM/BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details architectural considerations for building network-isolated AKS clusters. Explains integrating custom User-Defined Routes (UDR) and Azure Firewall to handle and monitor egress traffic. Essential for compliant financial or healthcare setups demanding rigorous data isolation.
#### VNet Peering

  - **(2022)** [blog.coffeeapplied.com: Securing AKS in peered virtual networks using only network security groups (NSGs)](https://blog.coffeeapplied.com/securing-aks-in-peered-virtual-networks-using-only-network-security-groups-nsgs-c43d6a215f32) <span class='md-tag md-tag--warning'>[BASH/ARM CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates locking down traffic inside peered Azure virtual networks utilizing Network Security Groups (NSGs) exclusively. Shows how to avoid routing complexity and high firewall transit charges in multi-tenant hub-and-spoke virtual environments.
## State and Data

### Database Virtualization

#### SQL Server and S3 Storage

  - **(2023)** [techcommunity.microsoft.com: SQL Server containers on Kubernetes with S3-compatible object storage - Getting started](https://techcommunity.microsoft.com/blog/sqlserver/sql-server-containers-on-kubernetes-with-s3-compatible-object-storage---getting-/3717003) <span class='md-tag md-tag--warning'>[SQL/YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Walks through deploying SQL Server containers inside Kubernetes using S3-compatible object storage for backups. Outlines durable storage configuration methods and provides an optimal blueprint for stateful data layer setups.
## Strategic Strategy

### Ecosystem News

#### Edge Kubernetes

  - **(2023)** [infoq.com: Microsoft Brings Kubernetes to the Edge with AKS Edge Essentials](https://www.infoq.com/news/2023/03/aks-edge-essentials-ga) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews the release of AKS Edge Essentials, Microsoft's lightweight managed Kubernetes distribution optimized for resource-constrained edge machines and industrial OT setups. Outlines how this strategy extends cloud-native operations directly to factory floors.
#### Pricing and SLA tiers

  - **(2023)** [techcommunity.microsoft.com: Azure Kubernetes Service Free tier and Standard tier](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-kubernetes-service-free-tier-and-standard-tier/3731432) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the structural and performance differences between the AKS Free and Standard pricing tiers. Analyzes the financial guarantees (SLAs), auto-scaler boundaries, and support systems required when migrating workloads to production environments.
#### Product Roadmap

  - **(2022)** [techcommunity.microsoft.com: Azure Kubernetes Service Microsoft Ignite announcements](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-kubernetes-service-microsoft-ignite-announcements/3650443) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Aggregates key product announcements, feature updates, and engineering roadmap directions announced at Microsoft Ignite targeting the AKS ecosystem. Discusses improved fleet operations, container scale, and identity controls.
### Enterprise Architecture

#### Automation and Runbooks

  - **(2022)** [buchatech.com/2022: A Guide to Navigating the AKS Enterprise Documentation & Scripts 🌟🌟](https://www.buchatech.com/2022/08/a-guide-to-navigating-the-aks-enterprise-documentation-scripts) <span class='md-tag md-tag--warning'>[POWERSHELL/BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive index highlighting central enterprise architecture runbooks, scripts, and Azure landing zone deployment models. Solves standard directory discovery hurdles for infrastructure teams architecting multi-cluster production layers.
#### First Steps

  - **(2021)** [adamtheautomator.com: Getting Started with the Azure Kubernetes Service (AKS)](https://adamtheautomator.com/azure-kubernetes-service) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive onboarding guide teaching foundational skills for deploying and managing an AKS cluster. Covers cluster creation, node pool verification, and basic CLI interactions. Designed to minimize onboarding friction for junior operators.
### Kubernetes Management

#### AKS Ecosystem

  - **(2021)** [thenewstack.io: Microsoft’s Practical Approach to Kubernetes Management](https://thenewstack.io/microsoft-takes-practical-approach-to-kubernetes-management) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An executive-level analysis exploring Microsoft's architecture philosophy in streamlining managed Kubernetes operations. Highlights historical shifts towards abstraction, fully managed control planes, and hybrid-cloud support via Azure Arc. Provides insight into AKS ecosystem management strategies.
## Strategy

### Platform Strategy

#### Adoption Frameworks

  - **(2022)** [digitalocean.com: Kubernetes for startups: Why, when, and how to adopt](https://www.digitalocean.com/resources/articles/kubernetes-for-startups) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural strategy guide assessing the costs and benefits of introducing Kubernetes inside early-stage startup ecosystems. Covers common mistakes like over-engineering cluster setups early on and maps out criteria for when to transition from PaaS tools to fully-managed Kubernetes environments.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Azure](./azure.md)

