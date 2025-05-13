
###############################################################################
#                                                                             #                                                                            
#                 R  Program  to  Score  the  PIRLS  2021  Items              #
#                         PIRLS  2021  User  Guide                            #
#                                                                             #                                                                               
#             For  use  with  PIRLS  2021  regular  files  (R5  suffix)       #
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
    output_file <- paste0(outdir,infile,"_SCR.Rdata")
    input_file <- paste0(indir,infile,".Rdata")
    
    #  Get  the  student  achievement  data
    load(input_file)
    data<-eval(as.symbol(infile))

    #  Score  multiple-choice  items  with  A  key
    #  paperPIRLS  items
    Aright <- c('RP21Y06',  'RP41O11',  'RP51D05',  'RP31M03',  'RP31M05',  'RP31M11',  'RP41B06',
                'RP41B12',  'RP51T09',  'RP51T14B', 'RP51T14C', 'RP51T14E', 'RP31U05',  'RP31U08',
                'RP41M09',  'RP41M18',  'RP51R08',  'RP51R14',  'RP31W09',  'RP31W12',  'RP41I06',
                'RP41I08',  'RP51N07',  'RP41E05',  'RP41E09',  'RP51C08',  'RP51C12',  'RP31P02',
                'RP41H03',  'RP41H04',  'RP41H07',  'RP41H10',  'RP41H13',  'RP51Z03')
    
    #  digitalPIRLS  items
    Aright <- c(Aright,
                'RE21Y06',  'RE41O11',  'RE51D05',  'RE31M03',  'RE31M05',  'RE31M11',  'RE41B06',
                'RE41B12',  'RE51T05A', 'RE51T05C', 'RE51T05E', 'RE51T09',  'RE51T14B', 'RE51T14C',
                'RE51T14E', 'RE31U05',  'RE31U08',  'RE31U12A', 'RE41M09',  'RE41M18',  'RE51R05A',
                'RE51R05B', 'RE51R05D', 'RE51R08',  'RE51R14',  'RE51R15D', 'RE31W09',  'RE31W12',
                'RE41I06',  'RE41I08',  'RE51N02A', 'RE51N02B', 'RE51N02D', 'RE51N06A', 'RE51N06B',
                'RE51N06D', 'RE51N07',  'RE51N10B', 'RE41E05',  'RE41E09',  'RE41E16D', 'RE51C01A',
                'RE51C01B', 'RE51C01E', 'RE51C07B', 'RE51C07D', 'RE51C08',  'RE51C12',  'RE31P02',
                'RE31P14C', 'RE41H03',  'RE41H04',  'RE41H07',  'RE41H10',  'RE41H13',  'RE51Z01A',
                'RE51Z01B', 'RE51Z01D', 'RE51Z03',  'E041R07C', 'E041R12',  'E041T12',  'E041T18B',
                'E041Z07',  'E041Z20B', 'E041Z20D', 'E051O02',  'E051O06',  'E051V09B', 'E051V09E',
                'E051V14',  'E051V17B', 'E051V17D', 'E051V17E', 'E051V18B')
    
    data <- scoreit(data, item=Aright, type="MC", right=1, NR=6, OM=9, other=7)
    
    
    #  Score  multiple-choice  items  with  B  key
    #  paperPIRLS  items
    Bright <- c('RP21Y01',  'RP21Y04',  'RP21Y05',  'RP21Y07',  'RP21Y11',  'RP41O06',  'RP51D02',  
                'RP51D09',  'RP31M01',  'RP31M07',  'RP31M15',  'RP41B10',  'RP51T02',  'RP51T07',  
                'RP51T14A', 'RP51T14D', 'RP31U02',  'RP31U13',  'RP41M05',  'RP41M11',  'RP41M15',  
                'RP51R11',  'RP31W08',  'RP51N03',  'RP21K06',  'RP21K09',  'RP21K11',  'RP41E04',  
                'RP51C02',  'RP31P08',  'RP31P10',  'RP41H05',  'RP41H15',  'RP51Z08')
    
    #  digitalPIRLS  items
    Bright <- c(Bright,
                'RE21Y01',  'RE21Y04',  'RE21Y05',  'RE21Y07',  'RE21Y11',  'RE41O06',  'RE51D02',  
                'RE51D09',  'RE31M01',  'RE31M07',  'RE31M15',  'RE41B10',  'RE51T02',  'RE51T05B',  
                'RE51T05D', 'RE51T07',  'RE51T14A', 'RE51T14D', 'RE31U02',  'RE31U12D', 'RE31U13',  
                'RE41M05',  'RE41M11',  'RE41M15',  'RE51R05C', 'RE51R05E', 'RE51R11',  'RE51R15C',  
                'RE31W08',  'RE51N02C', 'RE51N02E', 'RE51N03',  'RE51N06C', 'RE51N06E', 'RE51N10E',  
                'RE21K06',  'RE21K09',  'RE21K11',  'RE41E04',  'RE41E16E', 'RE51C01C', 'RE51C01D',  
                'RE51C02',  'RE51C07A', 'RE51C07C', 'RE31P08',  'RE31P10',  'RE31P14A', 'RE41H05',  
                'RE41H15',  'RE51Z01C', 'RE51Z01E', 'RE51Z08',  'E041R03D', 'E041R04',  'E041R07D',
                'E041R10',  'E041R13',  'E041T01',  'E041T13',  'E041T18D', 'E041Z01',  'E041Z11',  
                'E041Z15',  'E041Z20C', 'E051O03',  'E051O07',  'E051O16',  'E051V02',  'E051V05',  
                'E051V08',  'E051V09A', 'E051V09C', 'E051V09D', 'E051V12',  'E051V17A', 'E051V18C')
    
    data <- scoreit(data, item=Bright, type="MC", right=2, NR=6, OM=9, other=7)
    
    #  Score  multiple-choice  items  with  C  key
    #  paperPIRLS  items
    Cright <- c('RP21Y08',  'RP41O01',  'RP51D04',  'RP51D14',  'RP31M06',  'RP31M12',  'RP31M13',    
                'RP41B03',  'RP41B05',  'RP41B11',  'RP41B14',  'RP51T03',  'RP31U07',  'RP31U09',    
                'RP41M01',  'RP41M07',  'RP51R01',  'RP51R09',  'RP31W03',  'RP31W05',  'RP31W06',    
                'RP41I05',  'RP41I10',  'RP51N08',  'RP21K03',  'RP41E06',  'RP41E08',  'RP51C04',    
                'RP31P01',  'RP31P09',  'RP41H02',  'RP41H08',  'RP41H16',  'RP51Z04',  'RP51Z13')
    
    #  digitalPIRLS  items
    Cright <- c(Cright,
                'RE21Y08',  'RE41O01',  'RE51D04',  'RE51D14',  'RE31M06',  'RE31M12',  'RE31M13',  
                'RE41B03',  'RE41B05',  'RE41B11',  'RE41B14',  'RE51T03',  'RE31U07',  'RE31U09',  
                'RE31U12B', 'RE41M01',  'RE41M07',  'RE51R01',  'RE51R09',  'RE51R15A', 'RE31W03',  
                'RE31W05',  'RE31W06',  'RE41I05',  'RE41I10',  'RE51N08',  'RE51N10A', 'RE21K03',  
                'RE41E06',  'RE41E08',  'RE41E16A', 'RE51C04',  'RE31P01',  'RE31P09',  'RE31P14D',  
                'RE41H02',  'RE41H08',  'RE41H16',  'RE51Z04',  'RE51Z13',  'E041R01',  'E041R03C',  
                'E041R07A', 'E041T03',  'E041T16',  'E041T18A', 'E041Z05',  'E041Z08',  'E041Z18',  
                'E041Z20A', 'E051O14',  'E051V07',  'E051V18A', 'E051V18D')
    
    data <- scoreit(data=data, item=Cright, type="MC", right=3, NR=6, OM=9, other=7)
    
    #  Score  multiple-choice  items  with  D  key
    #  paperPIRLS  items
    Dright <- c('RP21Y02',  'RP41O12',  'RP51D08',  'RP31M08',  'RP31M14',  'RP41B02',  'RP51T06',  
                'RP51T08',  'RP31U03',  'RP31U06',  'RP41M02',  'RP41M13',  'RP51R06',  'RP51R10',  
                'RP31W10',  'RP41I02',  'RP41I12',  'RP21K04',  'RP21K08',  'RP41E03',  'RP41E11',  
                'RP41E17',  'RP51C09',  'RP51C11',  'RP31P05',  'RP41H09')
    
    #  digitalPIRLS  items
    Dright <- c(Dright,
                'RE21Y02',  'RE41O12',  'RE51D08',  'RE31M08',  'RE31M14',  'RE41B02',  'RE51T06',  
                'RE51T08',  'RE31U03',  'RE31U06',  'RE41M02',  'RE41M13',  'RE51R06',  'RE51R10',  
                'RE51R15E', 'RE31W10',  'RE41I02',  'RE41I12',  'RE51N10D', 'RE21K04',  'RE21K08',  
                'RE41E03',  'RE41E11',  'RE41E16C', 'RE41E17',  'RE51C09',  'RE51C11',  'RE31P05',  
                'RE41H09',  'E041R03A', 'E041R07B', 'E041T04',  'E041T11',  'E041T15',  'E041Z03', 
                'E041Z10',  'E041Z13',  'E051O01',  'E051O04',  'E051O15',  'E051V01',  'E051V11')
    
    data <- scoreit(data=data, item=Dright, type="MC", right=4, NR=6, OM=9, other=7)
    
    #  Score  multiple-choice  items  with  F  key
    #  digitalPIRLS  items
    Fright <- 'E041R03B'
    
    data <- scoreit(data=data, item=Fright, type="MC", right=6, NR=6, OM=9, other=7)
    
    #  Score  constructed-response  items
    #  paperPIRLS  items
    constr <- c('RP21Y03',  'RP21Y09',  'RP21Y10',  'RP21Y12',  'RP21Y13',  'RP21Y14',  'RP41O02',  
                'RP41O03',  'RP41O04',  'RP41O05',  'RP41O07',  'RP41O08',  'RP41O09',  'RP41O10',  
                'RP41O13',  'RP51D01',  'RP51D03',  'RP51D06',  'RP51D07',  'RP51D10',  'RP51D11',  
                'RP51D11A', 'RP51D11B', 'RP51D12',  'RP51D12A', 'RP51D12B', 'RP51D13',  'RP51D15',  
                'RP51D16',  'RP31M02',  'RP31M04',  'RP31M09',  'RP31M10',  'RP31M16',  'RP31M17',  
                'RP31M17A', 'RP31M17B', 'RP31M17C', 'RP41B01',  'RP41B04',  'RP41B07',  'RP41B08',  
                'RP41B09',  'RP41B13',  'RP41B15',  'RP41B16',  'RP41B17',  'RP51T01',  'RP51T04',  
                'RP51T05',  'RP51T10',  'RP51T11',  'RP51T12',  'RP51T13',  'RP51T14',  'RP51T15',  
                'RP51T16',  'RP31U01',  'RP31U04',  'RP31U10',  'RP31U11',  'RP31U12',  'RP31U14',  
                'RP41M03',  'RP41M04',  'RP41M06',  'RP41M08',  'RP41M10',  'RP41M12',  'RP41M14',  
                'RP41M16',  'RP41M17',  'RP51R02',  'RP51R03',  'RP51R04',  'RP51R05',  'RP51R07',  
                'RP51R13',  'RP51R15',  'RP51R16',  'RP51R17',  'RP51R17A', 'RP51R17B', 'RP31W01',  
                'RP31W02',  'RP31W04',  'RP31W07',  'RP31W07A', 'RP31W07B', 'RP31W07C', 'RP31W11',  
                'RP31W13',  'RP41I01',  'RP41I03',  'RP41I04',  'RP41I07',  'RP41I09',  'RP41I11',  
                'RP41I13',  'RP41I14',  'RP41I15',  'RP51N01',  'RP51N02',  'RP51N04',  'RP51N05',  
                'RP51N06',  'RP51N09',  'RP51N09A', 'RP51N09B', 'RP51N10',  'RP51N11',  'RP51N12',  
                'RP51N13',  'RP51N13A', 'RP51N13B', 'RP51N14',  'RP51N15',  'RP21K01',  'RP21K02',  
                'RP21K05',  'RP21K07',  'RP21K10',  'RP21K12',  'RP41E01',  'RP41E02',  'RP41E07', 
                'RP41E10',  'RP41E12',  'RP41E13',  'RP41E14',  'RP41E15',  'RP41E16',  'RP51C01',  
                'RP51C03',  'RP51C05',  'RP51C06',  'RP51C07',  'RP51C10',  'RP51C13',  'RP51C13A',  
                'RP51C13B', 'RP51C14',  'RP51C15',  'RP31P03',  'RP31P04',  'RP31P06',  'RP31P07',  
                'RP31P11',  'RP31P12',  'RP31P13',  'RP31P14',  'RP41H01',  'RP41H06',  'RP41H11',  
                'RP41H12',  'RP41H14',  'RP51Z01',  'RP51Z02',  'RP51Z05',  'RP51Z06',  'RP51Z07',  
                'RP51Z09',  'RP51Z10',  'RP51Z11',  'RP51Z12',  'RP51Z14',  'RP51Z15')
    
    #  digitalPIRLS  items
    constr <- c(constr,
                'RE21Y03',  'RE21Y09',  'RE21Y10',  'RE21Y12',  'RE21Y13',  'RE21Y14',  'RE41O02',  
                'RE41O03',  'RE41O04',  'RE41O05',  'RE41O07',  'RE41O08',  'RE41O09',  'RE41O10',  
                'RE41O13',  'RE51D01',  'RE51D03',  'RE51D06',  'RE51D07',  'RE51D10',  'RE51D11',  
                'RE51D11A', 'RE51D11B', 'RE51D12',  'RE51D12A', 'RE51D12B', 'RE51D13',  'RE51D15',  
                'RE51D16',  'RE31M02',  'RE31M04',  'RE31M09',  'RE31M10',  'RE31M16',  'RE31M17',  
                'RE31M17A', 'RE31M17B', 'RE31M17C', 'RE41B01',  'RE41B04',  'RE41B07',  'RE41B08',  
                'RE41B09',  'RE41B13',  'RE41B15',  'RE41B16',  'RE41B17',  'RE51T01',  'RE51T04',  
                'RE51T05',  'RE51T10',  'RE51T11',  'RE51T12',  'RE51T13',  'RE51T14',  'RE51T15',  
                'RE51T16',  'RE31U01',  'RE31U04',  'RE31U10',  'RE31U11',  'RE31U12',  'RE31U14',  
                'RE41M03',  'RE41M04',  'RE41M06',  'RE41M08',  'RE41M10',  'RE41M12',  'RE41M14',  
                'RE41M16',  'RE41M17',  'RE51R02',  'RE51R03',  'RE51R04',  'RE51R05',  'RE51R07',  
                'RE51R13',  'RE51R15',  'RE51R16',  'RE51R17',  'RE51R17A', 'RE51R17B', 'RE31W01',  
                'RE31W02',  'RE31W04',  'RE31W07',  'RE31W07A', 'RE31W07B', 'RE31W07C', 'RE31W11',  
                'RE31W13',  'RE41I01',  'RE41I03',  'RE41I04',  'RE41I07',  'RE41I09',  'RE41I11',  
                'RE41I13',  'RE41I14',  'RE41I15',  'RE51N01',  'RE51N02',  'RE51N04',  'RE51N05',  
                'RE51N06',  'RE51N09',  'RE51N09A', 'RE51N09B', 'RE51N10',  'RE51N11',  'RE51N12',  
                'RE51N13',  'RE51N13A', 'RE51N13B', 'RE51N14',  'RE51N15',  'RE21K01',  'RE21K02',  
                'RE21K05',  'RE21K07',  'RE21K10',  'RE21K12',  'RE41E01',  'RE41E02',  'RE41E07',  
                'RE41E10',  'RE41E12',  'RE41E13',  'RE41E14',  'RE41E15',  'RE41E16',  'RE51C01',  
                'RE51C03',  'RE51C05',  'RE51C06',  'RE51C07',  'RE51C10',  'RE51C13',  'RE51C13A',  
                'RE51C13B', 'RE51C14',  'RE51C15',  'RE31P03',  'RE31P04',  'RE31P06',  'RE31P07',  
                'RE31P11',  'RE31P12',  'RE31P13',  'RE31P14',  'RE41H01',  'RE41H06',  'RE41H11',  
                'RE41H12',  'RE41H14',  'RE51Z01',  'RE51Z02',  'RE51Z05',  'RE51Z06',  'RE51Z07',  
                'RE51Z09',  'RE51Z10',  'RE51Z11',  'RE51Z12',  'RE51Z14',  'RE51Z15',  'E041R02', 
                'E041R03',  'E041R05',  'E041R06',  'E041R07',  'E041R08',  'E041R09',  'E041R11', 
                'E041R14',  'E041R15',  'E041R16',  'E041T02',  'E041T05',  'E041T06',  'E041T08', 
                'E041T09',  'E041T10',  'E041T14',  'E041T17',  'E041T18',  'E041Z02',  'E041Z04', 
                'E041Z06',  'E041Z09',  'E041Z12',  'E041Z14',  'E041Z16',  'E041Z17',  'E041Z19', 
                'E041Z20',  'E051O05',  'E051O08',  'E051O09',  'E051O10',  'E051O11',  'E051O12', 
                'E051O13',  'E051O17',  'E051O18',  'E051V03',  'E051V04',  'E051V06',  'E051V09', 
                'E051V10',  'E051V13',  'E051V15',  'E051V16',  'E051V17',  'E051V18',  'E051V19A', 
                'E051V20')
    
    data <- scoreit(data=data, item=constr, type="CR", right="", NR=6, OM=9, other=7)
    
    # Save file
    env <- new.env()
    data_name <- paste0(infile,"_SCR")
    env[[data_name]] <- data
    save(list=c(data_name),envir=env,file=output_file)
}

doit(indir =  "<Specify location of input Rdata data file using format x:/xxx/>", 
     outdir = "<Specify location of output Rdata data file using format x:/xxx/>", 
     infile = "<Specify name of merged Rdata student achievement data file>")
