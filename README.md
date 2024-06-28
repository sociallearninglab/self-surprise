# Self-Surprise

## General points

- for folder and file names: 
	+ don't use white space in either folder or filenames, use an underscore "_" instead
	+ (almost always) use lower case only
- always use relative paths in your code
	+ for example, to save a figure from an R script inside the `code/R/` folder the path should be "../../figures/figure_name.pdf"
- keep your folder structure organized
	+ we recommend adhering to the folder structure in this repository 
	+ more complex projects may have additional folders such as `videos/`, `tables/`, ...
- note: some of the folders are empty except for a `.keep` file
	+ the `.keep` file is just there to make sure that github includes the otherwise empty folder 
	+ feel free to delete the `.keep` file once you've added another file to that folder
- each code subfolder has a readme file that should be updated with information about the code scripts 
- use github issues to keep track of any larger decisions that we make along the way 
- make sure to create a slack channel for each project, link up the github repository with the slack channel, and add the people working on the project to the github repo and slack channel 
- see our lab wiki for more help: https://github.com/cicl-stanford/wiki/wiki

## Repository structure 

```
├── code
├── data
├── figures
├── papers
├── presentation
└── writeup
```

### code 

Put all your code here. Use a separate folder for scripts based on the programming language. 

#### experiments 

The experiments folder is for the online (or in lab) experiments. Each experiment should be in its own folder. When you run another experiment, make sure to create a new folder (so that we always know what an experiment looked like when it was run). In readme file for the experiments folder, provide a brief summary of each experiment. Also note down any additional information that may not be saved within each experiment (e.g. how much the payment was for MTurk participants).

### data 

Put your raw data files here. Any data wrangling to that file should happen in your code scripts.

There are subfolders for each experiment, containing raw data in table format.

In the `box_drawing` subfolder, the data is split between two sheets, with the relevant differences being the date and the version of the script used. In both data sheets, the tables has the following columns:
- `ID`, the first column, refers to the ID number assigned to the subject in that row. This number is determined by the order in which subjects participate; it is arbitrary for anything other than identification purposes.
- `Sbj_initials`, the second column, contains the initials of the subject for that row. The convention is first initial and last initial, so for subjects with multiple last names, more than two letters may appear.
- The `Date` column contains the date on which the subject participated in the study, written in MM/DD/YYYY format.
- The `Duration` column contains the length of the experiment for each subject, written in minutes:seconds format.
- The `Script Version` column indicates what version of the task script the experiment used to run that trial of the experiment. Scripts are occassionally tweaked and updated, and this column clarifies which version was used. Links to existing scripts are as follows:
	- v1.0: https://docs.google.com/document/d/14PzlaPKJn_mRJrq7o3u1eqwYMGY2NOIRWqcJ5cjOJ8U/edit
	- v1.1: https://docs.google.com/document/d/10qGCRhbsQU-iwgjTPJbJ2Eg5zTXfJX6R_n0u5fiiui4/edit
	- v1.2: https://docs.google.com/document/d/1f_RExck9tISWX32G8PtJTduXlGGbzDidApR5Z3ln4Sc/edit
	- v1.3: https://docs.google.com/document/d/1qxSR5ftRd7R62ksblsltdppru05BUbfuax7Vr4S9144/edit
 	- v2.0: https://docs.google.com/document/d/19REw-8zXpKNuFg0ei-GoAGrdkE-3SoUXdKY_kotuHaE/edit
- The `Experimenter_initials` column contains the initials of the experimenter who ran each subject in the experiment.
- The `NOTES` column is a space for experimenters to write down any relevant information about that iteration of the experiment. For example, this section could include a note about equipment/experimenter error, or it could contain a note about the subject's behavior, if notable.
- The `peeking` column is answered with either `Yes` or `No`, signalling whether or not the subject attempted to peek beneath the box while they were drawing. This experiment involves the subject attempting to draw a straight line while unable to see what they are drawing, so it is important to note whether or not they tried to look during the drawing phase.
- The `Age_mos` column contains the subject's age in months.
- The `Gender` column contains either an `M` for male or an `F` for female, signifying the subject's assigned sex.
- The `Condition` column indicates whether the subject was in the control condition or the experimental condition. In the control condition, which is denoted by a 0, subjects are given a "drawing guide" made of two rulers to help them draw their line. In the experimental condition, indicated by a 1, subjects do not receive the help of a guide.
- The `Surprise_verbal` category indicates if, when asked, the subject responded that they were surprised by the outcome of their attempt to draw a straight line. `Yes` indicates that the participant was surprised by the result, while `No` indicates that they were not.
- If a subject says yes to the surprise question, they are asked a follow-up question to gauge how suprised they are. The `Suprise_verbal_graded` column contains the answers to this question. Experimenters give subjects three options (ex: "a little", "medium", "a lot"), and the subject's response is listed in this column. Options have varried slightly from script to script; scipt documents can be consulted for the options presented in each version. For subjects who said they were not surprised, this column is filled with a dash.
- The `Suprise_why` column contains answers to a follow-up question asking subjects why they were or were not surprised by the results of their drawing. Cells left blank indicate that the researcher did not ask this question.
- The `Actual_performance` column lists either `Success` or `Fail`/`Failure`, indicating whether or not the subject's actual drawing was a straight line connecting the dots, as instructed. This experiment involves swapping out the subject's actual drawing for a perfectly straight line, so all subjects are led to believe that they have succeeded. This column represents whether or not their true performance was a success.
- The `Surprise_expression` column indicates with a `Yes` or `No` whether or not the subject's facial expression looked surprised when their drawing was revealed. This category is intended as a check on the accuracy/authority of verbal responses in the `Surprise_verbal` column.
- The `Exploration_drawing_game` and `Exploration_tracing_game` pertain to the exploration phase of the experiment. After subjects have drawn their line and been shown the decoy drawing, they are allowed to choose between trying the same task again, or trying a novel task -- a connect-the-dot sheet. If the subject chooses to engage with the same task again, there will be a `Yes` in the `Exploration_drawing_game` column. If they choose to try the new task, there is a `Yes` in the `Exploration_tracing_game` column. It is possible for both columns to have a `Yes` (if the subject experiments with both), and it is also possible for both columns to have a `No` (i.e., if the subject chose not to engage with either option).
- The `Exploration_use_box` category signals whether a subject chose to use the box prop in the exploratory phase of the experiment. Empty cells in this column indicate that this column did not exist at the time of the experiment.
- Lastly, the `Exploration_check_out_box` column indicates whether or not subjects chose to examine the box prop while left alone for the exploration phase. Similar to the previous column, blank cells in this column indicate that it was added after those experiments were run.
  

In the `cards` subfolder, the data is contained in a sheet broken down into the following columns:
* `ID`: see box_drawing (above) for explanation
* `Sbj_initials`: see box_drawing (above) for explanation
* `Date`: see box_drawing (above) for explanation
* `Duration`: see box_drawing (above) for explanation
* The `Script ver` column serves the same purpose as the `Script Version` column from the box_drawing data sheets. The following are links to each existing task script for the card experiment:
	* v1.2: https://docs.google.com/document/d/1xNwy87b9ELjgRmofi06195TBFM0YVWIVJW_4Ohpa5F8/edit
	* v1.3: https://docs.google.com/document/d/14805mEIHWAD4M8qlzkz6L8BKoaDJQfoCx4QHU8YSsA4/edit
	* v1.4: https://docs.google.com/document/d/1k-dNcLDtSVnJhCL8VQKgrWXMgpjnnfpYXExy--Hvpgg/edit
 	* v2.0: https://docs.google.com/document/d/1g8riSaudx332AjaqfXe0TQBnB11R8RLt2P0jhikpHRI/edit
* `Exp_initials`: see `Experimenter_initials` decription from box_drawing (above) for explanation
* `NOTES`: see box_drawing (above) for explanation
* `Age`: see `Age_mos` category from box_drawing (above) for explanation
* `Gender`: see box_drawing (above) for explanation
* The `Cond_deck` category indicates which deck of cards was used for that subject. Both card decks used have 16 cards, four of which have stars on their fronts. The `No markers` option corresponds to a deck in which the backs of all 16 cards are identical, while the `Markers` answer indicates that the experiment used the control condition, a deck in which the four star cards are marked with star stickers on their backs.
* The `No of star cards picked` indicates how many star cards the subject was able to correctly identify when given four tries to pick out a card, looking only at the backs of the cards. Subjects run in the experimental condition (`No markers`) have a dash for this column, because in their condition, the results of the game are rigged to result in four stars cards as a result every time. Subjects in the control condition (`Markers`) have an integer between 0 and 4 in this category, indicating the number of star cards they identified.
*  `Surprise_verbal`: see box_drawing (above) for explanation
*  `Surprise_verbal_graded`: see box_drawing (above) for explanation
*  `Picking_strategy`: subjects were asked to explain the strategy that they used to pick their cards. Their answers are summarized in this column.
*  In the exploration phase of the cards experiment, subjects could choose to continue playing with the cards or to instead play with blocks. For script version 1.1 and 1.2,the blocks were a mix of metal and wood. From version 1.3 onwards, the blocks were wood only. The subjects played alone in the exploration phase. A `Yes` in the `Exploration_cards` column indicates that the subject chose to continue playing with the cards. A `Yes` in the `Exploration_blocks` column indicates that the subject chose to play with the blocks. It is possible to have a `Yes` in both columns, a `No` in both columns, or, most commonly, one of each.


In the `jumping` subfolder, the data sheet is divided into the following columns:
* `ID`: see box_drawing (above) for explanation
* `Subject_initials`: the same as `Sbj_initials` from cards and box_drawing
* `Date`: see box_drawing (above) for explanation
* `Experimenter_initials`: see box_drawing (above) for explanation
* `Age in months`: same as `Age` and `Age_mos` columns from cards and box_drawing, respectively
* `Gender`: see box_drawing (above) for explanation
* In the `How high do you THINK you can reach when you jump?` column, subjects were asked the title question. The experimenter moved their hand progressively lower on a measuring tape afixed to the wall, and instructed subjects to tell them when to stop. The height, in inches, of the stopping point is recorded in this column.
* In the `Reach with extended arm WITHOUT jumping` column, subjects were asked to stand next to the measuring tape and fully extend their arm upwards. The height, in inches, reached by the top of their hand is recorded in this column.
* In the `Reach with extended arm WITH jumping` column, subjects were asked to repeat the procedure from the previous column but then, with their arm still extended, to jump vertically as high as they could. The height reach by their hand at the peak of their jump is recorded in this column.
* The `Other notes` column is similar to the `NOTES` columns in cards and box_drawing; it is a space for the experimenter to take note of details that, while relevant, do not belong in any of the other columns.

### figures 

Save all your figures here. You may want to include additional subfolder here such as `plots/`, `diagrams/` etc. 

### papers 

Put research papers here that are relevant for your project. 

### presentation

Put your project presentation here (e.g. your keynote, powerpoint, google slides, or pdf file).

### writeup 

Put all your writing here. This folder structure is likely to expand for more complex projects. For example, you could add a subfolders like folders `journal/cognition/submission/`, `proceedings/cogsci/resubmission/` etc. 

## CRediT author statement 

Each public repository should have a [credit author statement](https://www.elsevier.com/authors/policies-and-guidelines/credit-author-statement) 

| Term                       | Definition                                                                                                                                                                                                    |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Conceptualization          | Ideas; formulation or evolution of overarching research goals and aims                                                                                                                                        |
| Methodology                | Development or design of methodology; creation of models                                                                                                                                                      |
| Software                   | Programming, software development; designing computer programs; implementation of the computer code and supporting algorithms; testing of existing code components                                            |
| Validation                 | Verification, whether as a part of the activity or separate, of the overall replication/ reproducibility of results/experiments and other research outputs                                                    |
| Formal analysis            | Application of statistical, mathematical, computational, or other formal techniques to analyze or synthesize study data                                                                                       |
| Investigation              | Conducting a research and investigation process, specifically performing the experiments, or data/evidence collection                                                                                         |
| Resources                  | Provision of study materials, reagents, materials, patients, laboratory samples, animals, instrumentation, computing resources, or other analysis tools                                                       |
| Data Curation              | Management activities to annotate (produce metadata), scrub data and maintain research data (including software code, where it is necessary for interpreting the data itself) for initial use and later reuse |
| Writing - Original Draft   | Preparation, creation and/or presentation of the published work, specifically writing the initial draft (including substantive translation)                                                                   |
| Writing - Review & Editing | Preparation, creation and/or presentation of the published work by those from the original research group, specifically critical review, commentary or revision – including pre-or postpublication stages     |
| Visualization              | Preparation, creation and/or presentation of the published work, specifically visualization/ data presentation                                                                                                |
| Supervision                | Oversight and leadership responsibility for the research activity planning and execution, including mentorship external to the core team                                                                      |
| Project administration     | Management and coordination responsibility for the research activity planning and execution                                                                                                                   |
| Funding acquisition        | Acquisition of the financial support for the project leading to this publication                                                                                                                              |

**Sample CRediT author statement**
- Zhang San: Conceptualization, Methodology, Software 
- Priya Singh: Data curation, Writing- Original draft preparation
- Wang Wu: Visualization, Investigation 
- Jan Jansen: Supervision 
- Ajay Kumar: Software, Validation
- Sun Qi: Writing-Reviewing and Editing


