<big><b> Author: Oweys Momenzada </big></b>

# Evergreen Classifier for German text corpus
<big><i> FOR DEEPER INSIGHT INTO THE WORK AND APPROACH, ALL NOTEBOOKS ARE WELL DOCUMENTED AND PROVIDED ON THIS GITHUB REPOSITORY. </i></big>

#### What is this repository about?
In my time at <a href="https://www.schickler.de/">SCHICKLER</a> I was allowed to work on the award-winning <a href="https://www.presseportal.de/pm/8218/4932175">DRIVE</a>-Project.
The Drive project has data from various regional publishers throughout Germany. 
One of my tasks was to develop an API in which customers search their archives for Evergreen articles. In addition, authors want to check how much evergreen character their written text contains.

##### What are Evergreens articles and why is a solution relevant?

Evergreen content is content that remains relevant regardless of the season or the time-frame (<a href="https://www.brainlabsdigital.com/blog/what-is-evergreen-content/#:~:text=Evergreen%20content%20definition,that%20never%20lose%20their%20leaves.">click here for more</a>). Thus, publishers can always use these articles without creating new ones. 

The challenge here is that such a project does not yet exist for German text corpus (it is also poorly documented for English text corpus). 
Therefore, this repository goes into detail about the technical approach. 

## Data
The Dataset has been labeled manually by the publishers. Therefore, I can not provide a dataset to work on. However, there is a dataset for English Evergreens
by <a href="https://www.kaggle.com/c/stumbleupon">StumbleUpon</a>. You should be able to apply my approach to the StumbleUpon Dataset.

As mentioned, the data is manually labeled. Only the text and the article-ID were used as dataset. For EDA purposes, further data, such as genre, publisher, accesses, etc., were taken from Google BigQuery. A labeled article could look as follows:


| ID | Text | Publisher  | pageview_start |  pageview_end  | genre | topic | label |
| ------------- | ------------- |------------- | ------------- |------------- | ------------- | ------------- | ------------- | 
| 55312 | Experte gibt Tipps für...  | Publisher 1  | 00:00:00 UTC | 00:00:20 UTC | Kultur | Tipps | Evergreen |
| 55442  | Zwei Schwerverletzte bei Unfall... | Publisher 3 | 03:00:10 UTC | 03:00:50 UTC | Gesellschaft | Nachrichten |  Ephemeral | 

Initially, a distinction was made between Evergreen-Seasonal, Evergreen-Forever, Evergeen-Event and Ephemeral.  However, after EDA (see <i>"/EDA/Evergreen EDA.ipynb"</i>), a too large disbalance of the data was noticed, which would have had an high impact on the accuracy of the model. Therefore, we only distinguish between Evergreens and Ephemeral or Non-Evergreens.

## Approach for the Classifier

### Time-based classification
After the EDA (see <i>"EDA/Evergreen EDA.ipynb"</i>), we could see that Evergreen articles behave differently in time than other articles. Evergreen articles have been more consistent in their views over time than other articles. Other articles have a high number of views in the first days and then drop significantly in the following days. Thus, you can classify Evergreen articles according to their behavior based on time. The problem is that, according to the results, the classification only can be reliable after 80 days of observation (see <i>"/EDA/Timebased Clf.ipynb"</i>). 

### Content-based classification
Therefore, we classify articles based on their content or text corpus. For the classification we will use the State-of-Art Model: <a href="https://arxiv.org/abs/1810.04805">BERT</a>. The advantage here is that a classification can be performed immediately. We could reach an accuracy of over 83% (see <i>"model/Model training.ipynb"</i>). 


## Real world Application, API & Deployment

A Real World Application on some articles can be seen  here "<i>Results and Examples.ipynb</i>"

This will be provided for SCHICKLERS customers based on an API. We first store the trained model into a Bucket in Google Cloud Storage and than load it into GCP AI Platform. We then implement Textcleaning and other Feature Engineering steps and also the communcation with the trained model on AI platform on a different .py-file (see <i>"Application - API/main.py"</i>). In addition, we use FLASK for our RESTful API. For our API we implement POST requests to get the text of our customers. We then finally deploy our API on APP Engine to provide for our customers online. 

&nbsp;

![Workflow](https://github.com/OweysMomenzada/Evergreen-Content-Classifier-for-german-Text/blob/main/EDA/images/Worfklow.png)


## Citing

Cite the authors the of BERT Model.
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

Please cite this GitHub if you use this work.
```
@misc{momenzada_schickler_2021_evergreen, 
      title={Evergreen recognition for German text}, 
      author={Momenzada, Oweys and SCHICKLER}, 
      url={https://github.com/OweysMomenzada/Evergreen-Content-Classifier-for-german-Text}, 
      journal={Github}, 
      year={2021}, 
      month={Sep}
      } 
```
