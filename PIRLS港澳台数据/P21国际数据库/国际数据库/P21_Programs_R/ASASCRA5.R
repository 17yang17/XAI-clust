
###############################################################################
#                                                                             #                                                                            
#             R  Program  to  Score  the  PIRLS  2021 Bridge  Items           #
#                     PIRLS  2021  User  Guide                                #
#                                                                             #                                                                               
#             For  use  with  PIRLS  2021  bridge  files  (A5  suffix)        #
#                                                                             #                                                                               
###############################################################################
library(tidyverse)

scoreit <- function(data, item, type, right, NR, OM, other){

  #  Code  for  multiple-choice  items
  if  (toupper(type)=="MC"){
    data <- data %>% mutate_at(vars(item), ~case_when ( . == right ~ 1,   # Item Key
                                                    . == NR    ~ NaN, # Not Reached
                                                    . == OM    ~ NaN, # Omitted
                                                    is.na(.)   ~ NaN, # Not Administered
                                                    . == other ~ 0,   # Other Missing
                                                    TRUE       ~ 0))
  }
  
  #  Code  for  constructed-response  items
  if  (toupper(type)=="CR"){
    data <- data %>% mutate_at(vars(item), ~case_when ( . == 3  ~ 3,      # 3 points
                                                    . == 2  ~ 2,      # 2 points
                                                    . == 1  ~ 1,      # 1 point
                                                    . == 0  ~ 0,      # No credit
                                                    . == NR ~ NaN,    # Not Reached
                                                    . == OM ~ NaN,    # Omitted
                                                    is.na(.) ~ NaN,   # Not Administered
                                                    . == other ~ 0,   # Other Missing
                                                    TRUE       ~ 0))
  }
  return(data)
}

doit <- function(indir=getwd(), outdir=getwd(), infile=""){
  output_file <- paste0(outdir, infile, "_SCR.Rdata")
  input_file <- paste0(indir, infile, ".Rdata")
  
  #  Get  the  student  achievement  data
  load(input_file)
  data <- eval(as.symbol(infile))
  
  #  Score  multiple-choice  items  with  A  key
  Aright <- c('RP21Y06',  'RP41O11',  'RP31M03',  'RP31M05',  'RP31M11',  'RP41B06', 'RP41B12',  
              'RP31W09',  'RP31W12',  'RP41I06',  'RP41I08',  'RP41E05', 'RP41E09')
  
  data <- scoreit(data=data,item=Aright, type="MC", right=1, NR=6, OM=9, other=7)
  
  
  #  Score  multiple-choice  items  with  B  key
  Bright <- c('RP21Y01',  'RP21Y04',  'RP21Y05',  'RP21Y07',  'RP21Y11',  'RP41O06',  'RP31M01',  
              'RP31M07',  'RP31M15',  'RP41B10',  'RP31W08',  'RP21K06',  'RP21K09',  'RP21K11',  
              'RP41E04')
  
  data <- scoreit(data=data, item=Bright, type="MC", right=2, NR=6, OM=9, other=7)
  
  #  Score  multiple-choice  items  with  C  key
  Cright <- c('RP21Y08',  'RP41O01',  'RP31M06',  'RP31M12',  'RP31M13',  'RP41B03',  'RP41B05',  
              'RP41B11',  'RP41B14',  'RP31W03',  'RP31W05',  'RP31W06',  'RP41I05',  'RP41I10',  
              'RP21K03',  'RP41E06',  'RP41E08')
 
  data <- scoreit(data=data, item=Cright, type="MC", right=3, NR=6, OM=9, other=7)
  
  #  Score  multiple-choice  items  with  D  key
  Dright <- c('RP21Y02',  'RP41O12',  'RP31M08',  'RP31M14',  'RP41B02', 'RP31W10',  'RP41I02',  
              'RP41I12',  'RP21K04',  'RP21K08',  'RP41E03',  'RP41E11', 'RP41E17')

  data <- scoreit(data=data, item=Dright, type="MC", right=4, NR=6, OM=9, other=7)

  #  Score  constructed-response  items
  constr <- c('RP21Y03',  'RP21Y09',  'RP21Y10',  'RP21Y12',  'RP21Y13',  'RP21Y14',  'RP41O02',  
              'RP41O03',  'RP41O04',  'RP41O05',  'RP41O07',  'RP41O08',  'RP41O09',  'RP41O10',  
              'RP41O13',  'RP31M02',  'RP31M04',  'RP31M09',  'RP31M10',  'RP31M16',  'RP31M17',  
              'RP31M17A', 'RP31M17B', 'RP31M17C', 'RP41B01',  'RP41B04',  'RP41B07',  'RP41B08',  
              'RP41B09',  'RP41B13',  'RP41B15',  'RP41B16',  'RP41B17',  'RP31W01',  'RP31W02',  
              'RP31W04',  'RP31W07',  'RP31W07A', 'RP31W07B', 'RP31W07C', 'RP31W11',  'RP31W13',  
              'RP41I01',  'RP41I03',  'RP41I04',  'RP41I07',  'RP41I09',  'RP41I11',  'RP41I13',  
              'RP41I14',  'RP41I15',  'RP21K01',  'RP21K02',  'RP21K05',  'RP21K07',  'RP21K10',  
              'RP21K12',  'RP41E01',  'RP41E02',  'RP41E07',  'RP41E10',  'RP41E12',  'RP41E13',  
              'RP41E14',  'RP41E15',  'RP41E16')
 
  data<-scoreit(data=data, item=constr, type="CR", right="", NR=6, OM=9, other=7)
  
  # Save file
  env <- new.env()
  data_name <- paste0(infile,"_SCR")
  env[[data_name]] <- data
  save(list=c(data_name), envir=env, file=output_file)
}

doit(indir =  "<Specify location of input Rdata data file using format x:/xxx/>", 
     outdir = "<Specify location of output Rdata data file using format x:/xxx/>", 
     infile = "<Specify name of merged Rdata student achievement data file>")

