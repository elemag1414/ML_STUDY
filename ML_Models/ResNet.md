# ResNet

[ResNet](http://www.arxiv.org/abs/1512.03385)은 2015년 ILSVRC Competition에서 우승한 모델이다.

Top-5 error율이 3.5%로 사람의 분류 수준인 5% 내외를 뛰어 넘는다.

Deep Learning 모델은 layer 수가 증가하면 성능이 향상된다고 알려졌다.
하지만, 네트워크를 깊게하면 back propagation시 gradient값이 작아지는
vanishing gradient 문제나 반대로 급격히 커져 네트워크가 수렴하지 않는
exploding 문제가 발생한다.

이를 해결하는 방법을 ResNet에서는 [Identity Mapping](https://arxiv.org/pdf/1603.05027.pdf)개념을 사용하는 skip connection을 통해
해결한다.

[[여기]](https://datascienceschool.net/view-notebook/958022040c544257aa7ba88643d6c032/)블로그에서 ResNet를 잘 정리하고 있으니, 참고

## Resnet Structures

Visualizations of network structures (tools from [ethereon](http://ethereon.github.io/netscope/quickstart.html)):

> [ResNet-50](http://ethereon.github.io/netscope/#/gist/db945b393d40bfa26006)

> [ResNet-101](http://ethereon.github.io/netscope/#/gist/b21e2aae116dc1ac7b50)

> [ResNet-152](http://ethereon.github.io/netscope/#/gist/d38f3e6091952b45198b)

## Deep Residual Networks Implementation

Visit [Kaiming He's Git](https://github.com/KaimingHe/deep-residual-networks)
