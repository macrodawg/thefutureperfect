# Master Modeler 2021 
## The Future Perfect: A Community Forward Approach to ERASE Child Trafficking 

_[****NEW: Check out our slide deck!****](https://docs.google.com/presentation/d/19SPfwN32y4M_-oad14gpWVdvJBZjMOaD1NKWL0Ji1FQ/edit?usp=sharing)_

_[****NEW: Check out the video walkthrough of our analysis!****](test.macrodawg.com/futureperfect.mp4)_


<p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/futureperfectreadme.png" width="350" title="The Future Perfect: Building a Better, Safer Future">
</p>

### Team Members:
<p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/Jasmine.png" width="200" title="Jasmine Cui">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/danielle.png" width="200" title="Danielle Handel">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/kellen.png" width="200" title="Kellen Sandvik">
</p>

<p align="center">
Jasmine Cui, Danielle Handel, Kellen Sandvik 
</p>

### Team Ethos: 

<p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/children.jpg" width="300" title="A child's rights are human rights.">
</p>

 Above all, we believe, firmly, that **a child's rights are human rights.**

To us, Master Modeler 2021 represents more than a competition — it is an opportunity to contribute our talents, our energy to a cause that is deeply meaningful and impactful. 

Thus, it goes without saying we put channeled our efforts into constructing a comprehensive, community forward solution to help ERASE Child Trafficking expand their platform while engaging stakeholders. 

Now more than ever, social media has been integrated into the fabric of our everyday lives — platforms like Facebook, Twitter, and Instagram allow those who have been diminished, sidelined, or otherwise pushed to the margins to reclaim their power, their voice. 

By helping ERASE expand and refine their social media approach we hope to play our small role in **restoring not only the safety, but also the dignity young, vulnerable people deserve.**

### Modeling Overview:  
 _(Model is located in future-perfect-modeling.Rmd in the 'code' folder of this repository)_

<p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/hashtags.png" width="650" title="Hashtag success!">
</p>
  
 Within the scope of our project, there are four main models which we have developed and the use case for each is as follows: 
 
 1. The Particulars: This is an OLS model that has been "partialed" out and constructed using a series of theoretically founded, OLS-estimated equations. These equations speak to key engagement patterns our team has identified by formalizing these patterns so that they are quantifiable and, most importantly, measurable. These equations can be used to elicit the causal relationships between a post's specific features and its likelihood of success. **This will allow ERASE to fine-tune their post strategy, allowing them to hone in on specific features of their content and identify how this might be related to that post's potential for success.**

2. The Bigger Picture: This is a fully integrated OLS model that can be used for broader, engagement prediction and, as illustrated, can be built into a form that will allow ERASE to upload drafts of posts, identify key characteristics of that post such as planned post time, and consequently predict how successful that post might be. **The specific deliverable our team is working on which uses this model will also use ERASE's inputs to make informed suggestions about post strategy to help ERASE maximize engagement in a legible, user-friendly way.** 

3. The Bigger, Better Picture: This random forest model serves as an alternative to the OLS model. The random forest approach is better suited for models which incorporate categorical covariates (e.g. post sentiment). **Notably, since we chose to place a great deal of emphasis around qualitative post characteristics such as emotions, our theoretical specification lends itself more to the random forest modeling approach due to its use of decision trees.** Even so, at this point in time, we believe this model is not as powerful as it could be due to the small size of the training dataset. While bigger is not  better in all cases, it is in the context of machine learning. Put simply, **computers do not have brains — they fumble around in the dark.** They need a lot of help and a lot of chances to get it right. 

**Like a genie that only grants hyper-specific wishes, machine learning methods require as much information as you can give them.** However, due Facebook's API limitations and security constraints, it is both slow and difficult to scrape data from "near and peer" pages. Thus, the overhead investment needed to optimally deploy this model is higher than that of the previous two models. 

4. "Hot or Not:" This probit model can be used to estimate a post's likelihood of achieving virality. Probit modeling allows us to specify a theoretical equation with a binary dependent variable. In this case, a post can be predicted to be "hot" or "not" on the basis of its features. Notably, the cutoff of virality is user defined and, consequently, may shift in line with ERASE's organizational goals or the evolution of the digital landscape. **Even so, this model may be useful if ERASE opts to make "viral" social media marketing a focal point of their stratagem** as many companies such as Oatly, Wendy's, and IHOP/IHOB have in recent years.

From a macro-perspective, these models are used to replicate, albeit simplistically, the complicated, dynamic relationships between users and ERASE's social media platforms. However, the rigor of the statistical theory, when deployed appropriately and combined with the power of human intuition, can clue us in to specific trends our own insight might even miss at first. 

As humans, while we have incredible intuition, we are limited by or physical needs. Consequently, we are equipped to see the trees and to understand them in detail. 
However, our capacity for insight is turbocharged by the power of modern technology. Through machine learning we take flight — suddenly, understanding the forest becomes a possibility. 

 <p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/datascience.jpg" width="300" title="Towards data science!">
</p>

### Plans For the Future: 
Ideally, we would love to continue to work with ERASE to extend the models we have built into **user-friendly tools** that will empower their team to continue drawing insights and refining their social media strategy beyond the scope of this competition. We have sketched out some ideas of how each model might be deployed and built into a dashboard. This would allow ERASE improve their strategy autonomously. For non-profits, autonomy is vital. 

Funds spent on hiring third party social media consultants or applications can and should be diverted towards the things that really matter — hiring more employees to manage casework, recovering those who are in danger, and, subsequently, helping the recovered heal. 

Concretely, we would like use our web-scraper in conjunction with Facebook's graph API to generate a **dynamic and updatable** .RDS file which will then funnel the latest information into our models such that **ERASE can understand how their social landscape is evolving in real time**. However, we understand that this is outside of the scope of Master Modeler 2021. 

Regardless, our team hopes that ERASE Child Trafficking is able to make use of our insights. Our greatest hope is that our project is able to allow them to **spread their word as far and wide** as possible. 

<p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/hope.png" width="300" title="Fighting for a better day!">
</p>

### Made With: R, Python, Jupyter, Care 
