#!/bin/bash

. DeployCluster.sh

sleep 3m

kubectl apply -f DeployRegistry.yaml
kubectl apply -f myjob.yaml

sleep 5m

kubectl -n kube-system create serviceaccount tiller
kubectl create clusterrolebinding tiller \
  --clusterrole cluster-admin \
  --serviceaccount=kube-system:tiller
helm init --service-account tiller

