<big><b> Author: Oweys Momenzada </big></b>

# Evergreen recognition for German text
<big><i> FOR DEEPER INSIGHT INTO THE WORK AND APPROACH, THE "PAPER_EVERGREEN_RECOGNIZER.PDF" IS PROVIDED ON THIS GITHUB REPOSITORY. </i></big>

#### What is this repository about?
In my time at <a href="https://www.schickler.de/">SCHICKLER</a> I was allowed to work on the award-winning <a href="https://www.presseportal.de/pm/8218/4932175">DRIVE</a>-Project.
The Drive project has data from various regional publishers throughout Germany. 
One of my tasks was to develop an API in which customers search their archives for Evergreen articles. In addition, authors want to check how much evergreen character their written text contains.

##### What are Evergreens articles and why is a solution relevant?

Evergreen content is content that remains relevant regardless of the season or the time-frame (<a href="https://www.brainlabsdigital.com/blog/what-is-evergreen-content/#:~:text=Evergreen%20content%20definition,that%20never%20lose%20their%20leaves.">click here for more</a>). Thus, publishers can always use these articles without creating new ones. 

The challenge here is that such a project does not yet exist for German texts (it is also poorly documented for English texts). 
Therefore, this repository goes into detail about the technical approach. 

## Approach for the Classifier

### Time-based classification
After the EDA (<i>EDA/Evergreen EDA.ipynb</i>), we could see that Evergreen articles behave differently in time than other articles. Evergreen articles have been more consistent in their views over time than other articles. Other articles have a high number of views in the first days and then drop significantly in the following days. So you can classify Evergreen articles according to their behavior based on time. The problem is that, according to our results, the classification only can be reliable after 80 days of observation (see <i>"/EDA/Timebased Clf.ipynb"</i>). 

### Time-based classification
Therefore, we classify articles based on their content or text corpus. For the classification we will use the State-of-Art Model: <a href="https://arxiv.org/abs/1810.04805">BERT</a>. The advantage here is that a classification can be performed immediately. We could get a accuracy of over 80% (see <i>"model/Model training.ipynb"</i>). 


## Real world Application, API & Deployment

A Real World Application on some articles can be seen  here "<i>Results and Examples.ipynb</i>"

We provide this for SCHICKLERS Customers based on an API. We first deploy the trained model on GCP AI Platform. We then implement Textcleaning and other Feature Engineering steps and also the communcation with the trained model on AI platform on a different .py-file (see <i>"Application - API/main.py"</i>). In addition, we use FLASK for our RESTful API. We then finally deploy our API on APP Engine to provide for our customers online. 

![Workflow](https://github.com/OweysMomenzada/Evergreen-Content-Classifier-for-german-Text/blob/main/EDA/images/Workflow.png)

## CONSIDER!
The Dataset has been labeled manually by the publishers. Therefore, I can not provide a dataset to work on. However, there is a dataset for english evergreens
by <a href="https://www.kaggle.com/c/stumbleupon">StumbleUpon</a>. You should be able to apply my approach to the StumbleUpon.

## Citing

Cite the authors the BERT Model.
``` 
@misc{devlin2019bert,
      title={BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding}, 
      author={Jacob Devlin and Ming-Wei Chang and Kenton Lee and Kristina Toutanova},
      year={2019},
      eprint={1810.04805},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

Please cite me if you use this work.
```
@misc{momenzada_schickler_2021, 
      title={Evergreen recognition for German text}, 
      author={Momenzada, Oweys and SCHICKLER}, 
      url={https://github.com/OweysMomenzada/Evergreen-Content-Classifier-for-german-Text}, 
      journal={Github}, 
      year={2021}, 
      month={Sep}
      } 
```
