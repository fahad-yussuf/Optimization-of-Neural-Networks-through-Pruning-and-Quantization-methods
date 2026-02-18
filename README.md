**Optimization of Neural Networks through Pruning and Quantization Methods.**
As neural networks grow in complexity and accuracy, their performance relies heavily on model parameters, which require substantial memory and computational power. 
For example, the widely used GPT-3 includes up to 175 billion parameters, a massive increase over previous models such as ResNet and LeNet. 
This trend leads us to assume that with improved models, the number of parameters will also continue to increase. 
The high cost and memory constraints are even more apparent when these models are deployed on devices with limited computational resources, energy, and bandwidth, such as mobile phones. 
This necessitates a need to optimize these networks, making them lightweight, all while still maintaining their accuracy. 
In this project, we sought to improve this by applying quantization and pruning techniques to a ResNet CNN model fine-tuned on CIFAR-10, 
not only on their own but also in tandem as we seek to find the best trade-off between performance and accuracy.
