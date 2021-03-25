# Master Modeler 2021 
## The Future Perfect: A Community Forward Approach to ERASE Child Trafficking 
_[****NEW: Check out our slide deck!****](https://docs.google.com/presentation/d/19SPfwN32y4M_-oad14gpWVdvJBZjMOaD1NKWL0Ji1FQ/edit?usp=sharing)_

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

Thus, it goes without saying we put channeled our efforts into constructing a comprehensive, community forward solution to help ERASE Child Trafficking expand their platform while engaging stakeholders. Now more than ever, social media has entered the fabric of our everyday lives — platforms like Facebook, Twitter, and Instagram have allowed those who have been diminished, sidelined, or otherwise pushed to the margins to reclaim the power of their voice. 

By helping ERASE expand and refine their social media approach we hope to play our small role in helping restore not only the safety, but also the dignity young, vulnerable people deserve. 

### Modeling Overview:  
 _(Model is located in future-perfect-modeling.Rmd in the 'code' folder of this repository)_
 
 <p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/datascience.jpg" width="300" title="Towards data science!">
</p>
  
 Within the scope of our project, there are four main models which we have developed and the use case for each is as follows: 
 
 1. The Particulars: This **partial OLS models** can be used to elicit the causal relationships between a post's specific features and its likelihood of success. **This will allow ERASE to fine-tune their post strategy by empowering them hone in on specific features of their content and identify how this might be related to that post's potential for success in terms of user engagement.**
On the other hand, 

2. The Bigger Picture: This **fully integrated OLS** model can be used for broader, engagement prediction and, as illustrated, can be build into a form that will allow ERASE to upload drafts of posts, identify key characteristics of that post such as planned post time, and consequently predict how successful that post might be. 

3. The Bigger, Better Picture: This **random forest model** serves as an alternative to the OLS model; however, the reason we provide this as an option is that the random forest approach is better suited to handle models which categorical covariates. **Notably, since we chose to place a great deal of emphasis around qualitative post characteristics such as emotions, our theoretical specification lends itself more to the Random Forest modeling approach due to its use of decision trees.** Even so, at this point in time, we believe the Random Forest model is not as powerful as it might be in the future due to the small size of the training data set. Like with most machine learning methods, Random Forest specification and estimation are best when a large training dataset is available. However, due to new limitations placed by Facebook on its API, it is difficult and slow to scrape data from near and peer pages and, thus, the overhead investment needed to deploy this model appropriately is higher than that of the OLS model. 

4. "Hot or Not:" This **probit** model we have specified speaks to the likelihood of a post achieving virality. Probit modeling allows us to specify a theoretical DGP with a binary dependent variable — if a post will go viral or not. Notably, the cutoff of virality is user defined and, consequently, may shift in line with ERASE's organizational standards or the evolution of the digital landscape. **Even so, this model may be useful if ERASE opts to make "viral" social media marketing a focal point of their stratagem** as many companies such as Oatly, Wendy's, and IHOP/IHOB have in recent years.

From a macro-perspective, these models are used to replicate, albeit simplistically, the complicated, dynamic relationships between users and ERASE's social media platforms. However, the rigor of the statistical theory we have "baked" into our models will clue us in to specific trends our own insight might even miss at first — we want to see the trees and the forest. 

### Plans For the Future: 
Ideally, we would love to continue to work with ERASE to extend the models we have built into **user-friendly tools** that will empower their team to continue drawing insights and refining their social media approach even beyond the scope of this competition. As of now, we have sketched out some ideas of how each model might be deployed and built into a dashboard which would allow ERASE to assess how well a post might do and to what extent. 

Concretely, we would like use our web-scraper in conjunction with Facebook's graph API to generate a **dynamic and updatable** .RDS file which will then funnel the latest information into our models such that ERASE can understand how their social landscape is evolving **in real time**. However, we understand that this is outside of the scope of Master Modeler 2021. 

Regardless, our team hopes that ERASE Child Trafficking is able to make use of our insights. Our greatest hope is that our project is able to allow them to spread their word as **far** and **wide** as possible. 

<p align="center">
  <img src="https://github.com/macrodawg/thefutureperfect/blob/main/images/hope.png" width="300" title="Fighting for a better day!">
</p>

### Made With: R, Python, Jupyter, Love 

