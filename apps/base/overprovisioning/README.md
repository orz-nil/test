# Overprovisioning
This application is maintained as a Helm chart - it is not a custom creation. Any changes made to the `resources/helm_template.yaml` files must be done with the following instructions.

# Rendering with Helm
1. `helm repo add cluster-proportional-autoscaler https://kubernetes-sigs.github.io/cluster-proportional-autoscaler`
1. `helm repo update`
1. `helm template overprovisioning cluster-proportional-autoscaler/cluster-proportional-autoscaler --values values.yaml --version 1.0.0 -n kube-system > resources/helm_output.yaml`
1. Extract any cluster-scoped resources from `resources/helm_output.yaml` (e.g. ClusterRole) and add them to the [overprovisioning cluster base](../../../cluster/base/overprovisioning)
