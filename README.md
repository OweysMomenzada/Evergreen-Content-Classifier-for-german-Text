# Evergreen-Content-Classifier-for-german-Text

#### What is this repository about?
In my time at <a href="https://www.schickler.de/">SCHICKLER</a> I was allowed to work on the award-winning <a href="https://www.presseportal.de/pm/8218/4932175">DRIVE</a>-Project.
The Drive project has data from various regional publishers throughout Germany. 
One of my tasks was to develop an API in which customers search their archives for Evergreen articles. In addition, authors want to check how much evergreen character their written text contains.

##### What are Evergreens articles and why is it relevant?

Evergreen content is content that remains relevant regardless of the season or the time-frame (<a href="https://www.brainlabsdigital.com/blog/what-is-evergreen-content/#:~:text=Evergreen%20content%20definition,that%20never%20lose%20their%20leaves.">click here for more</a>). Thus, publishers can always use these articles without creating new ones. 

The challenge here is that such a project does not yet exist for German texts (it is also poorly documented for English texts). 
Therefore, this repository goes into detail about the technical approach. 

## Approach for the Classifier

### Time-based classification
After the EDA (siehe ....), we could see that Evergreen articles behave differently in time than other articles. Evergreen articles have been more consistent in their views over time than other articles. Other articles have a high number of views in the first days and then drop significantly in the following days. So you can classify Evergreen articles according to their behavior based on time. The problem is that, according to our results, the classification only can be reliable after 80 days of observation (see....). 

### Time-based classification
Therefore, we classify articles based on their content or text corpus. For the classification we will use the State-of-Art Model: <a href="https://arxiv.org/abs/1810.04805">BERT</a>. The advantage here is that a classification can be performed immediately. We could get a accuracy of over 80%. 














## CONSIDER!
The Dataset has been labeled manually by the publishers. Therefore, I can not provide a dataset to work on. However, there is a dataset for english evergreens
by <a href="https://www.kaggle.com/c/stumbleupon">StumbleUpon</a>. You should be able to apply my approach to the StumbleUpon. 










## Experiments
We apply the approach on Benchmark dataset, thus we can only focus on the technical implementation and use it for comparison.  <br>
NOTE: I suggest to work on GPU for example on Google Colab (free GPU usage) to get the highest possible performance.
 
#### AmazonReview:
  ```
  Experiments\AmazonReview\GCMC-AmazonReview
  ```
#### Douban:
NOTE: Here I used the 10-Core approach, which may differ from author to author. 
  ```
  Experiments\Douban\GCMC-Douban
  ```
  
#### ML100K (with Features):
  ```
  Experiments\MovieLens100K\GCMC-MovieLens-100k
  
  Experiments\MovieLens100K\GCMC-MovieLens+Feature-100k
  ```
  
#### Yahoo Music:
  ```
  Experiments\AmazonReview\GCMC-Yahoo Music
  ```
  
## Research Paper
You can get deeper insight of our work <a href="https://www.dgl.ai/">here</a>.
This includes different types on Recommender-Systems, GNNs and Training methods.

## Cite
If you are interested and want to cite our work, please feel free to use:

  ```
  @article{loremipsum,
  title={loremipsum},
  author={vloremipsum},
  journal={loremipsum},
  year={loremipsum}
  }
  ```
  
If you are also interested in the model and the technical implementation based on the experiments also cite:
  
#### Authors of <a href="https://arxiv.org/abs/1909.01315">DGL</a>: 
  ```
  @misc{wang2020deep,
      title={Deep Graph Library: A Graph-Centric, Highly-Performant Package for Graph Neural Networks}, 
      author={Minjie Wang and Da Zheng and Zihao Ye and Quan Gan and Mufei Li and Xiang Song and Jinjing Zhou and Chao Ma and Lingfan Yu and Yu Gai and Tianjun Xiao and Tong He
  and George Karypis and Jinyang Li and Zheng Zhang},
      year={2020},
      eprint={1909.01315},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
  }
```
  
#### Authors of  the <a href="https://arxiv.org/abs/1706.02263">GCMC model</a>: 
``` 

  @article{vdberg2017graph,
  title={Graph Convolutional Matrix Completion},
  author={van den Berg, Rianne and Kipf, Thomas N and Welling, Max},
  journal={arXiv preprint arXiv:1706.02263},
  year={2017}
  }
```
