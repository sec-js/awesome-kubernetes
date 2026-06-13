# Kubernetes Networking

!!! info "Architectural Context"
    Detailed reference for Kubernetes Networking in the context of Networking & Service Mesh.

## Standard Reference

  - [Kubernetes Gateway API](https://github.com/kubernetes-sigs/gateway-api) <span class='md-tag md-tag--info'>⭐ 2861</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [InGate: Ingress & Gateway API Controller (Archived)](https://github.com/kubernetes-sigs/ingate) <span class='md-tag md-tag--info'>⭐ 731</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Introduction to Azure Application Gateway for Containers (AGC)](https://blog.cloudtrooper.net/2025/02/28/application-gateway-for-containers-a-not-so-gentle-intro-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Project Calico](https://www.projectcalico.org)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [AWS-VPC](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes Services and Load Balancing Explained](https://learnkube.com/kubernetes-services-and-load-balancing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ahmetb/kubernetes-network-policy-recipes 🌟](https://github.com/ahmetb/kubernetes-network-policy-recipes) <span class='md-tag md-tag--info'>⭐ 6139</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [dustinspecker.com: iptables: How Kubernetes Services Direct Traffic to Pods](https://dustinspecker.com/posts/iptables-how-kubernetes-services-direct-traffic-to-pods)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ronaknathani.com: How a Kubernetes Pod Gets an IP Address 🌟](https://ronaknathani.com/blog/2020/08/how-a-kubernetes-pod-gets-an-ip-address)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [arthurchiao.art: Cracking kubernetes node proxy (aka kube-proxy)](https://arthurchiao.art/blog/cracking-k8s-node-proxy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Transitioning from ingress-nginx to Traefik in Kubernetes](https://traefik.io/blog/transition-from-ingress-nginx-to-traefik)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Application Gateway for Containers with AKS Overlay Networking and VNet Flow Logs](https://blog.cloudtrooper.net/2025/04/02/application-gateway-for-containers-a-not-so-gentle-intro-4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Introducing Subnet Peering in Azure](https://techcommunity.microsoft.com/blog/azurenetworkingblog/introducing-subnet-peering-in-azure/4383841)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Private Link Reality Bites: Service Endpoints vs Private Link](https://blog.cloudtrooper.net/2025/02/17/private-link-reality-bites-service-endpoints-vs-private-link)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: The Kubernetes network model. How to implement the Kubernetes' networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Fighting Service Latency in Microservices With Kubernetes](https://medium.com/@sindhujacynixit/fighting-service-latency-in-microservices-with-kubernetes-f5a584f5af36)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Kubernetes NodePort vs LoadBalancer vs Ingress? When should' I use what? 🌟](https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.alexellis.io: Get a LoadBalancer for your private Kubernetes cluster](https://blog.alexellis.io/ingress-for-your-local-kubernetes-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dustinspecker.com: How Do Kubernetes and Docker Create IP Addresses?!](https://dustinspecker.com/posts/how-do-kubernetes-and-docker-create-ip-addresses)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Kubernetes Ingress Explained Completely For Beginners](https://www.youtube.com/watch?v=VicH6KojwCI)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Service Types in Kubernetes? 🌟](https://medium.com/faun/service-types-in-kubernetes-24a1587677d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [speakerdeck.com: Kubernetes and networks. Why is this so dan hard? 🌟](https://speakerdeck.com/thockin/kubernetes-and-networks-why-is-this-so-dang-hard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [eevans.co: Deconstructing Kubernetes Networking](https://eevans.co/blog/deconstructing-kubernetes-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [externalTrafficPolicy=local on kubernetes. How to preserve the source IP in kubernetes](https://blog.getambassador.io/externaltrafficpolicy-local-on-kubernetes-e66e498212f9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Why I use Ingress Controllers to expose Kubernetes services](https://opensource.com/article/20/8/ingress-controllers-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to setup Hetzner load balancer on a Kubernetes cluster](https://medium.com/@jmrobles/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [zhimin-wen.medium.com: Sticky Sessions in Kubernetes 🌟](https://zhimin-wen.medium.com/sticky-sessions-in-kubernetes-56eb0e8f257d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infoq.com: Kubernetes Ingress Is Now Generally Available](https://www.infoq.com/news/2020/09/kubernetes-ingress-ga)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jmrobles.medium.com: How to setup Hetzner load balancer on a Kubernetes' cluster](https://jmrobles.medium.com/how-to-setup-hetzner-load-balancer-on-a-kubernetes-cluster-2ce79ca4a27b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: Scaling Kubernetes Networking With EndpointSlices](https://kubernetes.io/blog/2020/09/02/scaling-kubernetes-networking-with-endpointslices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Create a Custom Annotation for the Kubernetes ingress-nginx Controller](https://medium.com/better-programming/creating-a-custom-annotation-for-the-kubernetes-ingress-nginx-controller-444e9d486192)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [haproxy.com: Announcing HAProxy Kubernetes Ingress Controller 1.5 🌟](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: HAProxy Kubernetes Ingress Controller Moves Outside the' Cluster](https://thenewstack.io/haproxy-kubernetes-ingress-controller-moves-outside-the-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [suse.com: NGINX Guest Blog: NGINX Kubernetes Ingress Controller 🌟](https://www.suse.com/c/nginx-guest-blog-kubernetes-ingress-controller)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudflare.com: Moving k8s communication to gRPC](https://blog.cloudflare.com/moving-k8s-communication-to-grpc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [K8GB - Kubernetes Global Balancer](https://github.com/AbsaOSS/k8gb) <span class='md-tag md-tag--info'>⭐ 1</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [altoros.com: Kubernetes Networking: How to Write Your Own CNI Plug-in with' Bash](https://www.altoros.com/blog/kubernetes-networking-writing-your-own-simple-cni-plug-in-with-bash)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Network Node Manager](https://github.com/kakao/network-node-manager) <span class='md-tag md-tag--info'>⭐ 109</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ithands-on.com: Kubernetes 101 : External services - ExternalName, DNS and' Endpoints](https://www.ithands-on.com/2021/04/kubernetes-101-external-services.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.googleblog.com: Kubernetes: Efficient Multi-Zone Networking with' Topology Aware Routing](https://opensource.googleblog.com/2020/11/kubernetes-efficient-multi-zone.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [nbailey.ca: Domesticated Kubernetes Networking](https://nbailey.ca/post/k8s-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sookocheff.com: A Guide to the Kubernetes Networking Model 🌟](https://sookocheff.com/post/kubernetes/understanding-kubernetes-networking-model)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [build.thebeat.co: A curious case of AWS NLB timeouts in Kubernetes](https://build.thebeat.co/a-curious-case-of-aws-nlb-timeouts-in-kubernetes-522bd88a3399)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ingressbuilder.jetstack.io 🌟🌟](https://ingressbuilder.jetstack.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Generating Kubernetes Network Policies Automatically By Sniffing' Network Traffic 🌟](https://itnext.io/generating-kubernetes-network-policies-by-sniffing-network-traffic-6d5135fe77db)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Using nginx-ingress controller to restrict access by IP (ip whitelisting)' for a service deployed to a Kubernetes (AKS) cluster](https://medium.com/@maninder.bindra/using-nginx-ingress-controller-to-restrict-access-by-ip-ip-whitelisting-for-a-service-deployed-to-bd5c86dc66d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [inlets.dev: Fixing Ingress for short-lived local Kubernetes clusters](https://inlets.dev/blog/2021/07/08/short-lived-clusters.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.teamhephy.info: Running Workflow Without Any LoadBalancer](https://blog.teamhephy.info/blog/posts/tutorials/running-workflow-without-any-loadbalancer.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Access Application Externally In Kubernetes Cluster using Load Balancer' Service](https://medium.com/codex/access-application-externally-in-kubernetes-cluster-using-load-balancer-service-d1b7858d51)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Why and How of Kubernetes Ingress (and Networking) 🌟](https://itnext.io/why-and-how-of-kubernetes-ingress-and-networking-6cb308ca03d2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [techdozo.dev: gRPC load balancing on Kubernetes (using Headless Service)](https://techdozo.dev/grpc-load-balancing-on-kubernetes-using-headless-service)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: ZeroLB, a New Decentralized Pattern for Load Balancing](https://thenewstack.io/zerolb-a-new-decentralized-pattern-for-load-balancing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ungleich.ch: Making kubernetes kube-dns publicly reachable](https://ungleich.ch/u/blog/kubernetes-making-dns-publicly-reachable)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ungleich.ch: Building Ingress-less Kubernetes Clusters](https://ungleich.ch/u/blog/kubernetes-without-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Ingress Controllers: The More the Merrier](https://thenewstack.io/ingress-controllers-the-more-the-merrier)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Setting up Application Load Balancer (Ingress)' for the Pods running in AWS EKS Fargate](https://levelup.gitconnected.com/setting-up-application-load-balancer-ingress-for-the-pods-running-in-aws-eks-fargate-519e20e97497)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: Kubernetes Ingress Tutorial For Beginners 🌟](https://devopscube.com/kubernetes-ingress-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ystatit.medium.com: How to Change Kubernetes Kube-apiserver IP Address](https://ystatit.medium.com/how-to-change-kubernetes-kube-apiserver-ip-address-402d6ddb8aa2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ithands-on.com: Kubernetes 101 : Changing a service type](https://www.ithands-on.com/2021/09/kubernetes-101-changing-service-type.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [technos.medium.com: Kubernetes Services for Absolute Beginners — NodePort' 🌟](https://technos.medium.com/kubernetes-services-for-absolute-beginners-nodeport-139b7060fe3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fransemalila.medium.com: Kubernetes Networking](https://fransemalila.medium.com/kubernetes-networking-cea2e1b7d2b3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Ingress Controllers: The Swiss Army Knife of Kubernetes](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/the-programmer: Working With ClusterIP Service Type In Kubernetes](https://medium.com/the-programmer/working-with-clusterip-service-type-in-kubernetes-45f2c01a89c8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [olamiko.medium.com: Technical Series: Kubernetes Networking](https://olamiko.medium.com/technical-series-kubernetes-networking-5a5dc3823163)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopslearners.com: Kubernetes Ingress Tutorial For Beginners](https://devopslearners.com/kubernetes-ingress-tutorial-for-beginners-26c2f7727bc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: How To Configure Ingress TLS/SSL Certificates in Kubernetes](https://devopscube.com/configure-ingress-tls-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armosec.io: Getting Started with Kubernetes Ingress | Ben Hirschberg](https://www.armosec.io/blog/kubernetes-ingress-beginners-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes Service Type LB for On Prem Deployments](https://itnext.io/kubernetes-service-type-lb-for-on-prem-deployments-89e9b2a73a0c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/techbeatly: Kubernetes Networking Fundamentals](https://medium.com/techbeatly/kubernetes-networking-fundamentals-d30baf8a28c8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [rajivsharma-2205.medium.com: Demystify how traffic reaches directly to pod' on using alb.ingress.kubernetes.io/target-type: ip](https://rajivsharma-2205.medium.com/demystify-how-traffic-reaches-directly-to-pod-on-using-alb-ingress-kubernetes-io-target-type-ip-f2d1be346b46)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/linux-shots: Kubernetes ingress as reverse proxy to Application' running outside cluster](https://medium.com/linux-shots/kubernetes-ingress-as-reverse-proxy-to-application-running-outside-cluster-206b6003f9cb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@zhaoyi0113: Kubernetes — How does service network work in the' cluster](https://medium.com/@zhaoyi0113/kubernetes-how-does-service-network-work-in-the-cluster-d235b69ff536)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@pavanbelagatti: Kubernetes Service Types Explained 🌟](https://medium.com/@pavanbelagatti/kubernetes-service-types-explained-2709cde3bc0c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tkng.io: The Kubernetes Networking Guide 🌟🌟](https://www.tkng.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tkng.io/arch: THE KUBERNETES NETWORK MODEL 🌟🌟](https://www.tkng.io/arch)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/stakater: Efficiently Expose Services on Kubernetes (part 1)' 🌟](https://medium.com/stakater/efficiently-expose-services-on-kubernetes-494a80f88aad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [platform9.com: Ultimate Guide to Kubernetes Ingress Controllers 🌟](https://platform9.com/blog/ultimate-guide-to-kubernetes-ingress-controllers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kubernetes Service Types Tutorial | Pavan Belagatti 🌟](https://faun.pub/kubernetes-service-types-tutorial-39223391316c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/slalom-build: Managing Ingress Traffic on Kubernetes Platforms' 🌟](https://medium.com/slalom-build/managing-ingress-traffic-on-kubernetes-platforms-ebd537cdfb46)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [craig-godden-payne.medium.com: How does ingress work in Kubernetes?](https://craig-godden-payne.medium.com/how-does-ingress-work-in-kubernetes-f3b121d0351f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dustinspecker.com: Kubernetes Networking from Scratch: Using BGP and BIRD' to Advertise Pod Routes](https://dustinspecker.com/posts/kubernetes-networking-from-scratch-bgp-bird-advertise-pod-routes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [home.robusta.dev: The ultimate guide to Kubernetes Services, LoadBalancers,' and Ingress 🌟🌟🌟](https://home.robusta.dev/blog/kubernetes-service-vs-loadbalancer-vs-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sanjimoh.medium.com: Demystifying Kubernetes Networking — Episode 1](https://sanjimoh.medium.com/demystifying-kubernetes-networking-episode-1-ca5605a97f87)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Tune up your Kubernetes Application Performance with a small DNS' Configuration](https://dev.to/imjoseangel/tune-up-your-kubernetes-application-performance-with-a-small-dns-configuration-1o46)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@mehmetodabashi: Kubernetes networking and service object: Understanding' ClusterIp and nodePort with hands on study](https://medium.com/@mehmetodabashi/kubernetes-networking-and-service-object-understanding-clusterip-and-nodeport-with-hands-on-study-90cfeaf66e8c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jasonmfehr: Inspecting Kubernetes Client to API Server Network' Traffic](https://medium.com/@jasonmfehr/inspecting-kubernetes-client-to-api-server-network-traffic-cd6d1802bb43)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: K8s Network — CNI Introduction](https://medium.com/geekculture/k8s-network-cni-introduction-b035d42ad68f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/patilswapnilv: Getting Started with Kubernetes Networking' 🌟](https://medium.com/patilswapnilv/getting-started-with-kubernetes-networking-7e10623fc78f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kubernetes Ingress with Nginx](https://faun.pub/kubernetes-ingress-with-nginx-3c77e703e91a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Inspecting and Understanding k8s Service Network 🌟](https://itnext.io/inspecting-and-understanding-service-network-dfd8c16ff2c5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ovidiuborlean.medium.com: Networking latency measurement in Kubernetes with' Sockperf plugin](https://ovidiuborlean.medium.com/networking-latency-measurement-in-kubernetes-with-sockperf-plugin-68283a0ed989)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Kubernetes networking deep dive: Did you make the right choice?](https://itnext.io/kubernetes-network-deep-dive-7492341e0ab5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@muhidabid.cs: Why does Kubernetes need Ingress?](https://medium.com/@muhidabid.cs/why-does-kubernetes-need-ingress-73d969fb6ffe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s — ipvs Mode Introduction](https://blog.devgenius.io/k8s-ipvs-mode-introduction-6457a02cd91a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [edureka.co: Kubernetes Networking – A Comprehensive Guide To The Networking' Concepts In Kubernetes](https://www.edureka.co/blog/kubernetes-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [whyk8s.substack.com: Why not DNS?](https://whyk8s.substack.com/p/why-not-dns)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: Kubernetes Gateway API: The Intro You Need To Read](https://medium.com/geekculture/kubernetes-gateway-api-the-intro-you-need-to-read-80965f7acd82)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ksingh7.medium.com: Kubernetes Endpoint Object: Your Bridge to External' Services 🌟🌟](https://ksingh7.medium.com/kubernetes-endpoint-object-your-bridge-to-external-services-3fc48263b776)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@ahmet16ck: What Is Load Balancer and How Does It Work In Kubernetes' ? 🌟](https://medium.com/@ahmet16ck/what-is-load-balancer-and-how-does-it-work-in-kubernetes-5ab5f0537069)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [api7.ai: How Does APISIX Ingress Support Thousands of Pod Replicas?](https://api7.ai/blog/apisix-ingress-support-thousands-pod-replicas)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/illuminations-mirror: Basic | Networking and Communication Between' Pods in Kubernetes](https://medium.com/illuminations-mirror/basic-networking-and-communication-between-pods-in-kubernetes-2e1627b03a87)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devops.dev: Networking in Kubernetes](https://blog.devops.dev/networking-in-kubernetes-55dcf794b9cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@mustafaaltunok: How Ingress, Service, Deployment and Pod Link' to each other](https://medium.com/@mustafaaltunok/how-ingress-service-deployment-and-pod-link-to-eachother-d3a6ae2c0e06)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [inlets.dev: How to Get Ingress for Private Kubernetes Clusters](https://inlets.dev/blog/2023/02/24/ingress-for-local-kubernetes-clusters.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devops.dev: Demystifying Kubernetes:Understanding Ingress, Configuration,' and Best Practices](https://blog.devops.dev/demystifying-kubernetes-understanding-ingress-configuration-and-best-practices-fb34e33e5f5f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/narasimha1997: Communication between Microservices in a Kubernetes' cluster 🌟](https://dev.to/narasimha1997/communication-between-microservices-in-a-kubernetes-cluster-1n41)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/google-cloud: Kubernetes Ingress Vs Gateway API 🌟](https://medium.com/google-cloud/kubernetes-ingress-vs-gateway-api-647ee233693d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/nerd-for-tech: Kubernetes: Deploying NGINX with a ConfigMap |' Chanel Jemmott](https://medium.com/nerd-for-tech/kubernetes-deploying-nginx-with-a-configmap-e8a2fe59bcb1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@sangjinn: How to communicate with Kubernetes workloads — Part' I. Service | Brandon Kang](https://medium.com/@sangjinn/how-to-communicate-with-kubernetes-workloads-1-service-abe1c5b03fc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [shahneil.medium.com: What Are Kubernetes Endpoints?](https://shahneil.medium.com/what-are-kubernetes-endpoints-and-how-to-use-them-a5a5da56f4d4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fr4nk.xyz: Understanding Ingress in Kubernetes: A Comprehensive Guide](https://fr4nk.xyz/understanding-ingress-in-kubernetes-a-comprehensive-guide-b23b5cf37f8d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Otterize: Intent-Based Access Control for Kubernetes and' Cloud](https://thenewstack.io/otterize-intent-based-access-control-for-kubernetes-and-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [community.ops.io: Kubernetes Ingress Controller. How does it work?=](https://community.ops.io/danielepolencic/learning-how-an-ingress-controller-works-by-building-one-in-bash-3fni)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@rasikzilte711: Kubernetes Networking — A Guide to Services,' Ingress, Network Policies, DNS, and CNI Plugins](https://medium.com/@rasikzilte711/kubernetes-networking-a-guide-to-services-ingress-network-policies-dns-and-cni-plugins-fc1ad7d22ab4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/codex: Capture tcpdump with ksniff and wireshark from Kubernetes](https://medium.com/codex/capture-tcpdump-with-ksniff-and-wireshark-from-kubernetes-c212b93ff9f9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudtechtwitter.com: Reverse Proxy vs. Forward Proxy: The Differences](https://www.cloudtechtwitter.com/2022/05/reverse-proxy-vs-forward-proxy.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [matthewpalmer.net: Kubernetes Networking Guide for Beginners](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-networking-guide-beginners.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Deciphering the Kubernetes Networking Maze: Navigating Load-Balance,' BGP, IPVS and Beyond](https://itnext.io/deciphering-the-kubernetes-networking-maze-navigating-load-balance-bgp-ipvs-and-beyond-7123ef428572)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [adil.medium.com: Network Traffic Shaping in Kubernetes: Topology Aware Routing](https://adil.medium.com/network-traffic-shaping-in-kubernetes-topology-aware-routing-e4ea4a03dd20)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.cloudsigma.com: Kubernetes DNS Service: A Beginner’s Guide](https://blog.cloudsigma.com/kubernetes-dns-service-a-beginners-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kuderko.medium.com: Fixing bad CPU usage distribution in Kubernetes 🌟](https://kuderko.medium.com/fixing-bad-cpu-usage-distribution-in-kubernetes-e1e43ed87cd6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com: Headless Kubernetes Service](https://medium.com/@bubu.tripathy/headless-k8s-service-924c689607a7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [goglides.dev: Headless services in Kubernetes Vs Regular Service: What,' Why, and How?](https://www.goglides.dev/bkpandey/headless-services-in-kubernetes-what-why-and-how-39fl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: What you need to know about Kubernetes NetworkPolicy](https://opensource.com/article/21/10/kubernetes-networkpolicy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: CKAD Scenarios about Ingress and NetworkPolicy](https://itnext.io/ckad-scenarios-about-ingress-and-networkpolicy-155ce958c9ce)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [whyk8s.substack.com: Why NetworkPolicies?](https://whyk8s.substack.com/p/why-networkpolicies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [yuminlee2.medium.com: Kubernetes Network Policies](https://yuminlee2.medium.com/kubernetes-network-policies-a93c2f588e31)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bagas-awibowo.medium.com: Helm — Templating Network Policy using Helm](https://bagas-awibowo.medium.com/helm-templating-network-policy-using-helm-783b2f7e401a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [NGINX Ingress Controller - v1.0.0](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.0.0) <span class='md-tag md-tag--info'>⭐ 19495</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span>
  - [amy-ma.medium.com: Nginx Ingress Configuration](https://amy-ma.medium.com/ingress-configuration-d9f13c5bcf1a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: How to Setup Nginx Ingress Controller On Kubernetes – Detailed' Guide 🌟](https://devopscube.com/setup-ingress-kubernetes-nginx-controller)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jonathan_37674: How to secure Kubernetes ingress? | By ARMO](https://medium.com/@jonathan_37674/how-to-secure-kubernetes-ingress-by-armo-cb86086ec540)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.backmarket.com: How we improved third-party availability and' latency with Nginx in Kubernetes 🌟](https://engineering.backmarket.com/how-we-improved-third-party-availability-and-latency-with-nginx-in-kubernetes-bb3fc7224ae4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [towardsdev.com: Kubernetes: Deploying Nginx Servers with ConfigMaps & Shared' Services with Minikube](https://towardsdev.com/kubernetes-deploying-nginx-servers-with-configmaps-shared-services-with-minikube-618aee9a8ff6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: How to Monitor and Alert on Ingress-NGINX in Kubernetes](https://faun.pub/how-to-monitor-and-alert-on-nginx-ingress-in-kubernetes-6d7d172f0399)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sumanprasad.hashnode.dev: A Beginner's Guide to Ingress and Ingress Controllers' in Kubernetes](https://sumanprasad.hashnode.dev/a-beginners-guide-to-ingress-and-ingress-controllers-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [akyriako.medium.com: Configure path-based routing with Nginx Ingress Controller](https://akyriako.medium.com/configure-path-based-routing-with-nginx-ingress-controller-64a63cd4d6bd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mattias.engineer: Kubernetes-101: Ingress 🌟](https://mattias.engineer/k8s/ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [trstringer.com: Kubernetes Ingress with Contour](https://trstringer.com/kubernetes-ingress-with-contour)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [gateway-api.sigs.k8s.io 🌟](https://gateway-api.sigs.k8s.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: Evolving Kubernetes networking with the Gateway API](https://kubernetes.io/blog/2021/04/22/evolving-kubernetes-networking-with-the-gateway-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Unifying Kubernetes Service Networking (Again) with the' Gateway API 🌟](https://thenewstack.io/unifying-kubernetes-service-networking-again-with-the-gateway-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.flomesh.io: Kubernetes Gateway API — Evolution of Service Networking](https://blog.flomesh.io/kubernetes-gateway-api-evolution-of-service-networking-aa76ec4efa7e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [armosec.io: The New Kubernetes Gateway API and Its Use Cases](https://www.armosec.io/blog/kubernetes-gateway-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/google-cloud: Security with Kubernetes Gateway API 🌟](https://medium.com/google-cloud/security-with-kubernetes-gateway-api-dcbb934ed2a4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [navendu.me: Comparing Kubernetes Gateway and Ingress APIs](https://navendu.me/posts/gateway-vs-ingress-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [NFTables mode for kube-proxy in Kubernetes](https://kubernetes.io/blog/2025/02/28/nftables-kube-proxy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Use Skupper to connect multiple Kubernetes clusters' 🌟](https://developers.redhat.com/blog/2021/04/20/use-skupper-to-connect-multiple-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Multi-Cluster Kubernetes Networking with Netmaker](https://itnext.io/multi-cluster-kubernetes-networking-with-netmaker-bfa4e22eb2fb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [howtoforge.com: Network Policy in Kubernetes 🌟](https://www.howtoforge.com/kubernetes_network_policy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to Provision Network Policies in Kubernetes | AWS 🌟](https://medium.com/avmconsulting-blog/exploring-network-policies-in-kubernetes-c8a3d8ed00cb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learncloudnative.com: Kubernetes Network Policy](https://www.learncloudnative.com/blog/2020-10-07-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [bionconsulting.com: Kubernetes Network Policies](https://www.bionconsulting.com/blog/kubernetes-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: The Kubernetes Network Security Effect 🌟](https://thenewstack.io/the-kubernetes-network-security-effect)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Control traffic flow to and from Kubernetes pods with Network' Policies](https://faun.pub/control-traffic-flow-to-and-from-kubernetes-pods-with-network-policies-bc384c2d1f8c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [loft-sh.medium.com: Kubernetes Network Policies: A Practitioner’s Guide' 🌟](https://loft-sh.medium.com/kubernetes-network-policies-a-practitioners-guide-c9bb4cdd0dbc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Kubernetes Network Policies: Are They Really Useful? 🌟](https://medium.com/codex/kubernetes-network-polices-are-they-really-useful-c3a153c49316)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [arthurchiao.art: Cracking Kubernetes Network Policy](https://arthurchiao.art/blog/cracking-k8s-network-policy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.mercari.com: Managing Network Policies for namespaces isolation' on a multi-tenant Kubernetes cluster](https://engineering.mercari.com/en/blog/entry/20220214-managing-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: Simplify Kubernetes Network Policy Generation](https://blog.devgenius.io/kubernetes-namespace-wide-network-policy-1126fafdf221)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.slycreator.com: Network Policies: Understanding Kubernetes Network' Policies](https://blog.slycreator.com/network-policies-understanding-kubernetes-network-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cilium.io: NetworkPolicy Editor: Create, Visualize, and Share Kubernetes' NetworkPolicies 🌟](https://cilium.io/blog/2021/02/10/network-policy-editor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Installing Cilium on Kubernetes in a fast and efficient way](https://itnext.io/installing-cilium-on-kubernetes-in-a-fast-and-efficient-way-dbcb79ce9699)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cilium.io: CNI Benchmark: Understanding Cilium Network Performance](https://cilium.io/blog/2021/05/11/cni-benchmark)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cockroachlabs.com: How to use Cluster Mesh for Multi-Region Kubernetes Pod' Communication](https://www.cockroachlabs.com/blog/cockroachdb-kubernetes-cilium)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cilium.io: Cilium 1.10: WireGuard, BGP Support, Egress IP Gateway, New Cilium' CLI, XDP Load Balancer, Alibaba Cloud Integration and more](https://cilium.io/blog/2021/05/20/cilium-110)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@charled.breteche: Kubernetes Security — Control pod to pod communications' with Cilium network policies](https://medium.com/@charled.breteche/kubernetes-security-control-pod-to-pod-communications-with-cilium-network-policies-d7275b2ed378)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [betterprogramming.pub: K8s: Network Policy Made Simple With Cilium Editor' 🌟](https://betterprogramming.pub/k8s-network-policy-made-simple-with-cilium-editor-a5b55781291c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Supporting the Evolving Ingress Specification in Kubernetes 1.18](https://kubernetes.io/blog/2020/06/05/supporting-the-evolving-ingress-specification-in-kubernetes-1.18)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Ingress service types in Kubernetes 🌟](https://medium.com/faun/ingress-service-types-in-kubernetes-3e9b68b78307)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Autoscaling Ingress Controllers in  Kubernetes (Daniele Polencic)](https://itnext.io/autoscaling-ingress-controllers-in-kubernetes-c64b47088485)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/stakater/Xposer](https://github.com/stakater/Xposer) <span class='md-tag md-tag--info'>⭐ 32</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [IP Address Management (IPAM)](https://en.wikipedia.org/wiki/IP_address_management)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes.io: Network Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Rancher CNI Providers 🌟](https://rancher.com/docs/rancher/v2.x/en/faq/networking/cni-providers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/containernetworking 🌟](https://github.com/containernetworking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: How to Understand and Set Up Kubernetes Networking 🌟](https://dzone.com/articles/how-to-understand-and-setup-kubernetes-networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Container Networking Interface aka CNI](https://medium.com/@vikram.fugro/container-networking-interface-aka-cni-bdfe23f865cf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Benchmark results of Kubernetes network plugins (CNI) over 10Gbit/s' network (Updated: August 2020)](https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-august-2020-6e1b757b9e49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Damn](https://github.com/nokia/danm) <span class='md-tag md-tag--info'>⭐ 393</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tigera.io](https://www.tigera.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Calico for Kubernetes networking: the basics & examples](https://medium.com/flant-com/calico-for-kubernetes-networking-792b41e19d69)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [projectcalico.org: Advertising Kubernetes Service IPs with Calico and BGP](https://www.projectcalico.org/advertising-kubernetes-service-ips-with-calico-and-bgp)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [mhmxs.blogspot.com: Autoscaling Calico Route Reflector topology in Kubernetes](https://mhmxs.blogspot.com/2020/12/autoscaling-calico-route-reflector.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tigera.io: Enforcing Network Security Policies with GitOps – Part 1 (Calico' + ArgoCD)](https://www.tigera.io/blog/enforcing-network-security-policies-with-gitops-part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s Networking — Calico (Part1)](https://blog.devgenius.io/k8s-networking-calico-part1-7f74395b6fe2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@arbnair97: Introduction to Kubernetes Network Policy and Calico' Based Network Policy](https://medium.com/@arbnair97/introduction-to-kubernetes-network-policy-and-calico-based-network-policy-675a7fa6b5dc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to Autoscale the DNS Service in a Kubernetes Cluster](https://medium.com/faun/how-to-autoscale-the-dns-service-in-a-kubernetes-cluster-cbb46ae89678)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Supercharge CoreDNS with Cluster Addons 🌟](https://thenewstack.io/supercharge-coredns-with-cluster-addons)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iamitcohen.medium.com: DNS in Kubernetes, how does it work?](https://iamitcohen.medium.com/dns-in-kubernetes-how-does-it-work-7c4690fd813e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [nslookup.io: The life of a DNS query in Kubernetes](https://www.nslookup.io/learning/the-life-of-a-dns-query-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [levelup.gitconnected.com: Kubernetes with CoreDNS](https://levelup.gitconnected.com/kubernetes-with-coredns-e40772c5e6ee)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes Node Local DNS Cache](https://povilasv.me/kubernetes-node-local-dns-cache)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [k8gb.io](https://www.k8gb.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.abaganon.com: Why you probably won’t use K8gb.io](https://blog.abaganon.com/going-global-with-kubernetes-490cf51e2bf8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to/aws-builders: Amazon VPC Lattice — Build Applications, Not Networks](https://dev.to/aws-builders/amazon-vpc-lattice-build-applications-not-networks-59j8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [NetMaker](https://github.com/gravitl/netmaker) <span class='md-tag md-tag--info'>⭐ 11581</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>

## Cloud Infrastructure

### Kubernetes

#### Networking

  - [cilium.io](https://cilium.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An eBPF-powered open-source project that provides high-performance, secure, and observable networking, load balancing, and network security for Kubernetes workloads. Cilium is widely adopted by enterprise platforms due to its scale capabilities and granular L3-L7 policy controls.
## Cloud Native

### Networking (1)

#### Kubernetes (1)

##### Ingress Controllers

  - **(2022)** [ovh.com - getting external traffic into kubernetes: clusterip, nodeport, loadbalancer and ingress](https://blog.ovhcloud.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep conceptual dive comparing methods to route traffic into a Kubernetes cluster. Details ClusterIP (internal), NodePort (static port mapping), LoadBalancer (provider cloud ingress integration), and Ingress Controllers (routing based on HTTP paths/host headers), evaluating performance trade-offs.
## Cloud Native Infrastructure

### Networking (2)

#### Egress Traffic Control

##### Case Studies

  - [Controlling outbound traffic from Kubernetes](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly regarded engineering case study by Monzo bank detailing how they designed and operated egress gateways to control and audit outbound traffic. Explains compliance benefits, custom proxy layers, and high-availability engineering patterns.
## Cloud Native Security

### Network Security

#### Network Policies

  - [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith' to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines a methodology to empirically test and verify active Kubernetes Network Policies. Details the usage of programmatic probes to transition network security evaluation from abstract policy syntax configurations to verifiable network boundaries.
## Networking (3)

### CNI

#### Calico

  - **(2020)** [**thenewstack.io: Tigera's Calico Aims to Ease Connectivity Pain with Kubernetes**](https://thenewstack.io/kubernetes) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Covers Tigera Calico's core value proposition of delivering flexible, secure CNI capabilities for Kubernetes environments. It contrasts Calico's IP-in-IP and BGP routing modes with standard encapsulation overlays, providing optimal performance. Integrates advanced security policy engines capable of running in both Kubernetes and hybrid virtualized clusters.
#### Flannel

  - **(2025)** [==Flannel==](https://github.com/flannel-io/flannel) <span class='md-tag md-tag--info'>⭐ 9454</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Flannel is a highly stable, lightweight Layer 3 network fabric designed specifically for Kubernetes. It runs a simple agent on each host to allocate subnet leases, supporting backends like VXLAN, host-gw, and UDP. While lacking advanced L7 policy capabilities, its extreme simplicity makes it a favorite for bootstrapping lightweight development and bare-metal environments.
### DNS

#### Monitoring

  - **(2021)** [**sysdig.com: How to monitor coreDNS 🌟**](https://www.sysdig.com/blog/how-to-monitor-coredns) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Illustrates methods for monitoring CoreDNS performance within Kubernetes clusters using Prometheus metrics. Focuses on critical golden signals like request rate, latency, packet dropouts, and cache hit/miss ratios. Essential for preventing cluster-wide DNS exhaustion bottlenecks which can degrade microservice lookup times.
### IPAM

#### Automated Workflows

  - **(2023)** [fusionlayer.com: Software-Defined IP Address Management (IPAM)](https://www.fusionlayer.com/products/infinity) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — FusionLayer Infinity provides centralized Software-Defined IP Address Management (IPAM) tailored for modern cloud networks and multi-orchestrator environments. It automates network and IP provisioning across distributed container infrastructures and edge data centers. This mitigates IP exhaustion and overlapping CIDR conflicts while bridging legacy networks with automated Kubernetes workloads.
### Ingress

#### Comparison

  - **(2021)** [blog.palark.com: Comparing Ingress controllers for Kubernetes](https://palark.com/blog/comparing-ingress-controllers-for-kubernetes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive comparative matrix of popular Kubernetes ingress controllers, including NGINX, Traefik, HAProxy, Contour, and Envoy-based proxies. It benchmarks them against metrics like protocol support (gRPC, HTTP/2, WebSockets), security, dynamic updates, and ease of deployment. Ideal for system architects choosing an ingress gateway for custom runtime workloads.
#### Envoy

  - **(2023)** [getenroute.io: Drive API Security At Kubernetes Ingress Using Helm And Envoy 🌟](https://docs.getenroute.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Enroute, an Envoy-based API gateway and ingress controller for Kubernetes. Detail includes securing APIs at the edge using Helm charts to deploy and configure rate-limiting, JWT authentication, and CORS policies. It provides a lightweight, performant alternative to heavy API management gateways by coupling Envoy's speed with Kubernetes-native CRDs.
#### Fundamentals

  - **(2022)** [searchitoperations.techtarget.com: Differences between Kubernetes Ingress vs. load balancer](https://www.techtarget.com/searchitoperations/feature/Differences-between-Kubernetes-Ingress-vs-load-balancer) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Clarifies the architectural differences between raw Kubernetes LoadBalancer services and Ingress resources. It outlines the cost and operational trade-offs of using external cloud-provider load balancers versus consolidated application-layer routing inside the cluster. Crucial for infrastructure planners looking to optimize both cloud spend and traffic routing strategies.
#### HAProxy

  - **(2021)** [devclass.com: HAProxy Ingress Controller 1.5 introduces mTLS support, gives load balancing experts more power](https://www.devclass.com/containers/2021/01/26/haproxy-ingress-controller-15-introduces-mtls-support-gives-load-balancing-experts-more-power/1619777) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Covers the release of HAProxy Ingress Controller 1.5, focusing on enterprise-grade mTLS implementation for zero-trust traffic control. It explores advanced routing capabilities, client certificate verification, and low-level performance tuning options designed for high-throughput load balancing. This update bridges the gap between traditional edge proxying and cloud-native ingress management.
#### NGINX

  - **(2022)** [**loft.sh: Kubernetes NGINX Ingress: 10 Useful Configuration Options 🌟**](https://www.vcluster.com/blog/kubernetes-nginx-ingress) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Provides 10 practical configurations for optimizing the ubiquitous NGINX Ingress Controller. It details custom annotations for rate-limiting, body-size limits, SSL redirection, CORS, and header manipulation. This technical guide serves as a quick reference for hardening and scaling web traffic paths into Kubernetes clusters.
#### OpenShift

  - **(2020)** [**openshift.com: gRPC or HTTP/2 Ingress Connectivity in OpenShift 🌟**](https://www.redhat.com/en/blog/grpc-or-http/2-ingress-connectivity-in-openshift) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Focuses on establishing end-to-end gRPC and HTTP/2 transport over Red Hat OpenShift Ingress and HAProxy routers. It details the TLS termination strategies and ALPN negotiations required to maintain streaming connections. Essential for high-performance microservice communication within OpenShift SDN and OVN-Kubernetes topologies.
#### Traefik

  - **(2020)** [**containo.us: Kubernetes Ingress & Service API Demystified**](https://traefik.io/blog/kubernetes-ingress-service-api-demystified) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Evaluates the core architecture of Kubernetes Ingress resources and Service APIs, illustrating how they interact with reverse proxies. It highlights Traefik's implementation of ingress specifications, demystifying route matching, load balancing, and dynamic configuration discovery. Offers deep structural comparison between legacy Ingress and modern patterns.
### Ingress Controllers (1)

#### Comparison (1)

  - [Learnk8s: Comparison of Kubernetes Ingress controllers 🌟](https://docs.google.com/spreadsheets/d/191WWNpjJ2za6-nbG4ZoUMXMpUK8KlCIosvQB0f-oq3k/edit#gid=907731238) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An industry-standard comparison spreadsheet analyzing over a dozen Kubernetes Ingress controllers. Details performance, dynamic reloading capabilities, routing protocols, and native TLS/WAF integrations.
### Load Balancing

#### Multi-Cluster

  - **(2021)** [**cloud.redhat.com: Global Load Balancer Approaches 🌟**](https://www.redhat.com/en/blog/global-load-balancer-approaches) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Compares various global load balancing (GSLB) architectures for multi-cluster and multi-region Kubernetes deployments. The analysis highlights DNS-based routing, Anycast IP routing, and hybrid CDN-integrated load balancers. Addresses disaster recovery, latency-based routing, and failover topologies necessary for highly resilient cloud-native systems.
### Security

#### Cilium Network Policy

  - **(2024)** [==editor.cilium.io 🌟==](https://editor.networkpolicy.io) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A visual designer created by Cilium to simplify the drafting of complex Kubernetes and Cilium-specific NetworkPolicies. It translates service dependencies into valid Kubernetes YAML rules, helping developers minimize security gaps. Highly recommended for multi-tier microservice infrastructures requiring visual validation before CI/CD deployment.
#### Namespace Isolation

  - **(2022)** [**loft.sh: Kubernetes Network Policies for Isolating Namespaces 🌟**](https://www.vcluster.com/blog/kubernetes-network-policies-for-isolating-namespaces) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Focuses exclusively on namespace-level isolation techniques using declarative Network Policies. It shows how to enforce strict multi-tenancy boundaries in shared staging or production clusters, preventing unauthorized inter-namespace discovery and communication. Highlights optimal configuration patterns to ensure strict compliance.
#### Network Policies (1)

  - **(2022)** [**loft.sh: Kubernetes Network Policies: A Practitioner's Guide 🌟**](https://www.vcluster.com/blog/kubernetes-network-policies-a-practitioners-guide) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A comprehensive practical guide covering the execution and isolation mechanics of Kubernetes Network Policies. Step-by-step instructions detail how default-deny structures work, how selector matching functions, and how to test rules in staging. Empowers operators to block lateral movement of attackers within microservice deployments.
#### OpenShift (1)

  - **(2020)** [openshift.com: Network Policies: Controlling Cross-Project Communication on OpenShift](https://www.redhat.com/en/blog/network-policies-controlling-cross-project-communication-on-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to write and apply Network Policies to control namespace and cross-project isolation in Red Hat OpenShift. It covers ingress/egress restriction, labels, and integration with OpenShift SDN multi-tenant plugins. Protects multi-tenant workloads by applying rigid segmentation rules at the container network interface layer.
#### Packet Management

  - **(2023)** [otterize.com: Mastering Kubernetes networking: A journey in cloud-native packet management](https://www.cyera.com) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores deep-packet cloud-native networking with an emphasis on intent-based access controls and service-to-service communication. Discusses how modern Kubernetes clusters secure network pathways through dynamic declarative policies. Offers structural insight into how packet-level visibility helps identify data leakage and configuration drift.
### Service Mesh

#### Linkerd

  - **(2023)** [**buoyant.io: Kubernetes network policies with Cilium and Linkerd**](https://www.buoyant.io/blog/kubernetes-network-policies-with-cilium-and-linkerd) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Highlights the cooperative synergy of deploying the Linkerd service mesh alongside Cilium's eBPF-based CNI. It details how to leverage Cilium for Layer 3/4 packet filtration and Linkerd for Layer 7 mTLS identity validation. This dual-layered framework provides maximum defense-in-depth security with minimal networking latency overhead.
### Services

#### Fundamentals (1)

  - **(2021)** [sysdig.com: Kubernetes Services: ClusterIP, Nodeport and LoadBalancer](https://www.sysdig.com/blog/kubernetes-services-clusterip-nodeport-loadbalancer) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demystifies core Kubernetes service types: ClusterIP, NodePort, and LoadBalancer. It demonstrates how kube-proxy manipulates iptables or IPVS configurations to achieve internal service discovery and round-robin load balancing. Helps operators grasp how traffic finds containerized workloads from both inside and outside the IP address space.
### Traffic Flow

#### Troubleshooting

  - **(2023)** [==learnk8s.io: Tracing the path of network traffic in Kubernetes 🌟==](https://learnkube.com/kubernetes-network-packets) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Offers an exceptional, granular breakdown of how network packets flow through a Kubernetes cluster. From physical network interfaces to IPVS/iptables rules and CNI-driven packet encapsulation (overlay vs. underlay), this visual guide untangles pod-to-pod and external traffic paths. Highly valuable for deep debugging of cluster network failures.
## Observability

### Cost Optimization

#### Data Storage

  - **(2023)** [instana.com: The Hidden Cost of Observability: Data Volume](https://www.ibm.com/think) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the economic and architectural implications of high-cardinality and high-volume observability data. Provides strategies for dynamic rate limiting, smart sampling, and metric deduplication to prevent telemetry storage costs from scaling linearly with microservices growth.

---
💡 **Explore Related:** [Cloudflare](./cloudflare.md) | [Servicemesh](./servicemesh.md) | [Networking](./networking.md)

