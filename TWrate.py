#! /usr/bin/env python



###################################################################
##								 ##
## Name: TWrate.py						 ##
## Author: Kevin Nash 						 ##
## Date: 6/5/2012						 ##
## Purpose: This program creates eta binned tags and probes 	 ##
##          as a function of Pt for data and MC for use with 	 ##
##          TWrate_Maker.py.					 ##
##								 ##
###################################################################

import os
import glob
import math
from math import sqrt,exp
import ROOT
from ROOT import std,ROOT,TFile,TLorentzVector,TMath,gROOT, TF1,TH1F,TH1D,TH2F,TH2D
from ROOT import TVector
from ROOT import TFormula

import sys
from DataFormats.FWLite import Events, Handle
from optparse import OptionParser
from array import *

parser = OptionParser()

parser.add_option('-s', '--set', metavar='F', type='string', action='store',
                  default	=	'data',
                  dest		=	'set',
                  help		=	'dataset (ie data,ttbar etc)')
parser.add_option('-u', '--ptreweight', metavar='F', type='string', action='store',
                  default	=	'none',
                  dest		=	'ptreweight',
                  help		=	'on or off')
parser.add_option('-t', '--trigger', metavar='F', type='string', action='store',
                  default	=	'none',
                  dest		=	'trigger',
                  help		=	'none, nominal, up, or down')
parser.add_option('-n', '--num', metavar='F', type='string', action='store',
                  default	=	'all',
                  dest		=	'num',
                  help		=	'job number')
parser.add_option('-j', '--jobs', metavar='F', type='string', action='store',
                  default	=	'1',
                  dest		=	'jobs',
                  help		=	'number of jobs')
parser.add_option('-g', '--grid', metavar='F', type='string', action='store',
                  default	=	'off',
                  dest		=	'grid',
                  help		=	'running on grid off or on')
parser.add_option('-c', '--cuts', metavar='F', type='string', action='store',
                  default	=	'rate_default',
                  dest		=	'cuts',
                  help		=	'Cuts type (ie default, rate, etc)')


(options, args) = parser.parse_args()



print "Options summary"
print "=================="
for  opt,value in options.__dict__.items():
	#print str(option)+ ": " + str(options[option]) 
	print str(opt) +': '+ str(value)
print "=================="
print ""

#If running on the grid we access the script within a tarred directory
di = ""
if options.grid == 'on':
	di = "tardir/"
	sys.path.insert(0, 'tardir/')

gROOT.Macro(di+"rootlogon.C")
import Bstar_Functions	
from Bstar_Functions import *

#Load up cut values based on what selection we want to run 
Cuts = LoadCuts(options.cuts)
wpt = Cuts['wpt']
tpt = Cuts['tpt']
dy = Cuts['dy']
tmass = Cuts['tmass']
nsubjets = Cuts['nsubjets']
tau32 = Cuts['tau32']
tau21 = Cuts['tau21']
minmass = Cuts['minmass']
sjbtag = Cuts['sjbtag']
wmass = Cuts['wmass']
eta1 = Cuts['eta1']
eta2 = Cuts['eta2']


#For large datasets we need to parallelize the processing
jobs=int(options.jobs)
if jobs != 1:
	num=int(options.num)
	jobs=int(options.jobs)
	print "Running over " +str(jobs)+ " jobs"
	print "This will process job " +str(num)
else:
	print "Running over all events"


#Based on what set we want to analyze, we find all Ntuple root files 
files = Load_Ntuples(options.set)
if (options.set.find('ttbar') != -1) or (options.set.find('singletop') != -1):
	settype = 'ttbar'
elif (options.set.find('QCD') != -1):
	settype ='QCD'
else :
	settype = options.set.replace('right','').replace('left','')

print 'The type of set is ' + settype

if options.set != 'data':
	#Load up scale factors (to be used for MC only)

	TrigFile = TFile(di+"TRIG_EFFICWPHTdata_dijet8TeV.root")
	TrigPlot = TrigFile.Get("r11")

	PileFile = TFile(di+"PileUp_Ratio_"+settype+".root")
	PilePlot = PileFile.Get("Pileup_Ratio")




# We select all the events:    
events = Events (files)

#Here we load up handles and labels.
#These are used to grab entries from the Ntuples.
#To see all the current types in an Ntuple use edmDumpEventContent /PathtoNtuple/Ntuple.root

puHandle    	= 	Handle("int")
puLabel     	= 	( "ttbsmAna", "npvRealTrue" )

CA8Handle     	= 	Handle( "vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > >")
CA8Label      	= 	( "nsub", "CA8P4" )

TopTau2Handle       = 	Handle( "std::vector<double>" )
TopTau2Label    	= 	( "nsub" , "Tau2")

TopTau3Handle       = 	Handle( "std::vector<double>" )
TopTau3Label    	= 	( "nsub" , "Tau3")

TopTau1Handle       = 	Handle( "std::vector<double>" )
TopTau1Label    	= 	( "nsub" , "Tau1")



#Load all hemisphere 0 objects
#---------------------------------------------------------------------------------------------------------------------#

hemis0topHandle     	= 	Handle( "vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > >")
hemis0topLabel      	= 	( "ttbsmAna", "topTagP4Hemis0" )


hemis0TopBDiscsj0CSVHandle       = 	Handle( "std::vector<double>" )
hemis0TopBDiscsj0CSVLabel    	= 	( "ttbsmAna", "topTagsj0BDiscCSVHemis0")

hemis0TopBDiscsj1CSVHandle       = 	Handle( "std::vector<double>" )
hemis0TopBDiscsj1CSVLabel    	= 	( "ttbsmAna", "topTagsj1BDiscCSVHemis0")

hemis0TopBDiscsj2CSVHandle       = 	Handle( "std::vector<double>" )
hemis0TopBDiscsj2CSVLabel    	= 	( "ttbsmAna", "topTagsj2BDiscCSVHemis0")

hemis0TopBDiscsj3CSVHandle       = 	Handle( "std::vector<double>" )
hemis0TopBDiscsj3CSVLabel    	= 	( "ttbsmAna", "topTagsj3BDiscCSVHemis0")

hemis0NSubJetsHandle 	= 	Handle (  "vector<double> "  )
hemis0NSubJetsLabel  	= 	( "ttbsmAna" , "topTagNSubjetsHemis0")

hemis0MinMassHandle     = 	Handle( "std::vector<double>" )
hemis0MinMassLabel  	= 	( "ttbsmAna", "topTagMinMassHemis0" )

hemis0TopMassHandle     = 	Handle( "std::vector<double>" )
hemis0TopMassLabel  	= 	( "ttbsmAna", "topTagTopMassHemis0" )

hemis0prCA8Handle  	= 	Handle ("vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > >")
hemis0prCA8Label    	=	( "ttbsmAna", "wTagP4Hemis0" )


#---------------------------------------------------------------------------------------------------------------------#


# Load all Hemisphere 1 objects
#---------------------------------------------------------------------------------------------------------------------#

hemis1topHandle     	= 	Handle( "vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > >")
hemis1topLabel      	= 	( "ttbsmAna", "topTagP4Hemis1" )


hemis1TopBDiscsj0CSVHandle       = 	Handle( "std::vector<double>" )
hemis1TopBDiscsj0CSVLabel    	= 	( "ttbsmAna", "topTagsj0BDiscCSVHemis1")

hemis1TopBDiscsj1CSVHandle       = 	Handle( "std::vector<double>" )
hemis1TopBDiscsj1CSVLabel    	= 	( "ttbsmAna", "topTagsj1BDiscCSVHemis1")

hemis1TopBDiscsj2CSVHandle       = 	Handle( "std::vector<double>" )
hemis1TopBDiscsj2CSVLabel    	= 	( "ttbsmAna", "topTagsj2BDiscCSVHemis1")

hemis1TopBDiscsj3CSVHandle       = 	Handle( "std::vector<double>" )
hemis1TopBDiscsj3CSVLabel    	= 	( "ttbsmAna", "topTagsj3BDiscCSVHemis1")

hemis1NSubJetsHandle 	= 	Handle (  "vector<double> "  )
hemis1NSubJetsLabel  	= 	( "ttbsmAna" , "topTagNSubjetsHemis1")

hemis1MinMassHandle     = 	Handle( "std::vector<double>" )
hemis1MinMassLabel  	= 	( "ttbsmAna", "topTagMinMassHemis1" )

hemis1TopMassHandle     = 	Handle( "std::vector<double>" )
hemis1TopMassLabel  	= 	( "ttbsmAna", "topTagTopMassHemis1" )

hemis1prCA8Handle     	= 	Handle( "vector<ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > >")
hemis1prCA8Label      	= 	( "ttbsmAna", "wTagP4Hemis1" )

GenHandle = Handle( "vector<reco::GenParticle>" )
GenLabel = ( "prunedGenParticles", "" )
#---------------------------------------------------------------------------------------------------------------------#

#Create the output file
if jobs != 1:
	f = TFile( "TWratefile"+options.set+"_job"+options.num+"of"+options.jobs+"_PSET_"+options.cuts+".root", "recreate" )
else:
	f = TFile( "TWratefile"+options.set+"_PSET_"+options.cuts+".root", "recreate" )




print "Creating histograms"

#Define Histograms
f.cd()
#---------------------------------------------------------------------------------------------------------------------#
pteta1pretag          = TH1D("pteta1pretag",           "b Probe pt in 0<Eta<1.0",             400,  0,  2000 )
pteta2pretag          = TH1D("pteta2pretag",           "b Probe pt in 0.6<Eta<2.4",             400,  0,  2000 )

pteta1          = TH1D("pteta1",           "b pt in 0<Eta<1.0",             400,  0,  2000 )
pteta2          = TH1D("pteta2",           "b pt in 1.0<Eta<2.4",             400,  0,  2000 )


pteta1pretag.Sumw2()
pteta2pretag.Sumw2()


pteta1.Sumw2()
pteta2.Sumw2()


MtwwptcomparepreSB1e1    = TH2F("MtwwptcomparepreSB1e1",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )
MtwwptcomparepostSB1e1    = TH2F("MtwwptcomparepostSB1e1",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )

MtwwptcomparepreSB1e1.Sumw2()
MtwwptcomparepostSB1e1.Sumw2()

MtwwptcomparepreSB1e2    = TH2F("MtwwptcomparepreSB1e2",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )
MtwwptcomparepostSB1e2    = TH2F("MtwwptcomparepostSB1e2",  "Comparison wpt and Mtw",   		400,0,2000,  140,  500,  4000 )

MtwwptcomparepreSB1e2.Sumw2()
MtwwptcomparepostSB1e2.Sumw2()




#---------------------------------------------------------------------------------------------------------------------#

# loop over events
#---------------------------------------------------------------------------------------------------------------------#

count = 0
jobiter = 0
print "Start looping"
#initialize the ttree variables
tree_vars = {"wpt":array('d',[0.]),"wmass":array('d',[0.]),"tpt":array('d',[0.]),"tmass":array('d',[0.]),"tau32":array('d',[0.]),"tau21":array('d',[0.]),"nsubjets":array('d',[0.]),"sjbtag":array('d',[0.]),"weight":array('d',[0.])}


Tree = Make_Trees(tree_vars)
totevents = events.size()
print str(totevents)  +  ' Events total'
for event in events:
    count	= 	count + 1

   # Uncomment for a low count test run
    #if count > 5000:
	#break

    if count % 100000 == 0 :
      print  '--------- Processing Event ' + str(count) +'   -- percent complete ' + str(100*count/totevents) + '% -- '

    #Here we split up event processing based on number of jobs 
    #This is set up to have jobs range from 1 to the total number of jobs (ie dont start at job 0)
    if jobs != 1:
    	if (count - 1) % jobs == 0:
		jobiter+=1
	count_index = count - (jobiter-1)*jobs
	if count_index!=num:
		continue 
	
    #We load up the relevant handles and labels and create collections
    event.getByLabel (hemis1prCA8Label, hemis1prCA8Handle)
    wJetsh1 		= 	hemis1prCA8Handle.product()

    event.getByLabel (hemis0prCA8Label, hemis0prCA8Handle)
    wJetsh0 		= 	hemis0prCA8Handle.product()
    
    event.getByLabel (hemis1topLabel, hemis1topHandle)
    topJetsh1 		= 	hemis1topHandle.product()

    event.getByLabel (hemis0topLabel, hemis0topHandle)
    topJetsh0 		= 	hemis0topHandle.product()
    


    bjh0 = 0
    bjh1 = 0

    #Require 1 pt>150 jet in each hemisphere (top jets already have the 150GeV requirement) 

    for wjet in wJetsh0:
	if wjet.pt() > 150.0:
		bjh0+=1
    for wjet in wJetsh1:
	if wjet.pt() > 150.0:
		bjh1+=1

    njets11b0 	= 	((len(topJetsh1) == 1) and (bjh0 == 1))
    njets11b1 	= 	((len(topJetsh0) == 1) and (bjh1 == 1))
    #We consider both the case that the b is the leading (highest pt) jet (hemis0) and the case where the top is the leading jet (hemis1)
    for hemis in ['hemis0','hemis1']:
    	if hemis == 'hemis0'   :
		if not njets11b0:
			continue 
		#The Ntuple entries are ordered in pt, so [0] is the highest pt entry
		#We are calling a candidate b jet (highest pt jet in hemisphere0)  
		wjet = wJetsh0[0]

		tjet = topJetsh1[0]
        	TopMassLabel = hemis1TopMassLabel
		TopMassHandle = hemis1TopMassHandle
        	NSubJetsLabel = hemis1NSubJetsLabel
		NSubJetsHandle = hemis1NSubJetsHandle 
        	MinMassLabel = hemis1MinMassLabel
		MinMassHandle = hemis1MinMassHandle
    		TopBDiscsj0CSVLabel = hemis1TopBDiscsj0CSVLabel
		TopBDiscsj0CSVHandle = hemis1TopBDiscsj0CSVHandle
    		TopBDiscsj1CSVLabel = hemis1TopBDiscsj1CSVLabel
		TopBDiscsj1CSVHandle = hemis1TopBDiscsj1CSVHandle
    		TopBDiscsj2CSVLabel = hemis1TopBDiscsj2CSVLabel
		TopBDiscsj2CSVHandle = hemis1TopBDiscsj2CSVHandle
    		TopBDiscsj3CSVLabel = hemis1TopBDiscsj3CSVLabel
		TopBDiscsj3CSVHandle = hemis1TopBDiscsj3CSVHandle


    	if hemis == 'hemis1'  :
		if not njets11b1:
			continue 
		wjet = wJetsh1[0]

		tjet = topJetsh0[0]
        	TopMassLabel = hemis0TopMassLabel
		TopMassHandle = hemis0TopMassHandle
        	NSubJetsLabel = hemis0NSubJetsLabel
		NSubJetsHandle = hemis0NSubJetsHandle 
        	MinMassLabel = hemis0MinMassLabel
		MinMassHandle = hemis0MinMassHandle
    		TopBDiscsj0CSVLabel = hemis0TopBDiscsj0CSVLabel
		TopBDiscsj0CSVHandle = hemis0TopBDiscsj0CSVHandle
    		TopBDiscsj1CSVLabel = hemis0TopBDiscsj1CSVLabel
		TopBDiscsj1CSVHandle = hemis0TopBDiscsj1CSVHandle
    		TopBDiscsj2CSVLabel = hemis0TopBDiscsj2CSVLabel
		TopBDiscsj2CSVHandle = hemis0TopBDiscsj2CSVHandle
    		TopBDiscsj3CSVLabel = hemis0TopBDiscsj3CSVLabel
		TopBDiscsj3CSVHandle = hemis0TopBDiscsj3CSVHandle

	if abs(wjet.eta())>2.40 or abs(tjet.eta())>2.40:
		continue

    	weight=1.0
	#Cuts are loaded from the Bstar_Functions.py file
	#here wpt[0] is 370 and wpt[1] is inf, so we are making sure the b pt is at least 370 GeV
    	wpt_cut = wpt[0]<wjet.pt()<wpt[1]
    	tpt_cut = tpt[0]<tjet.pt()<tpt[1]
    	dy_cut = dy[0]<=abs(tjet.Rapidity()-wjet.Rapidity())<dy[1]
    	#We first perform the top and b candidate pt cuts and the deltaY cut
    	if wpt_cut and tpt_cut and dy_cut: 
		if options.set!="data":
			#Pileup reweighting is done here 
			event.getByLabel (puLabel, puHandle)
    			PileUp 		= 	puHandle.product()
                	bin1 = PilePlot.FindBin(PileUp[0]) 
			weight *= PilePlot.GetBinContent(bin1)

        	event.getByLabel (TopMassLabel, TopMassHandle)
        	topJetMass 	= 	TopMassHandle.product()
        	event.getByLabel ( NSubJetsLabel , NSubJetsHandle )
    		NSubJets 		= 	NSubJetsHandle.product()
        	event.getByLabel (MinMassLabel, MinMassHandle)
    		topJetMinMass 	= 	MinMassHandle.product()
		tmass_cut = tmass[0]<topJetMass[0]<tmass[1]
		nsubjets_cut = nsubjets[0]<=NSubJets[0]<nsubjets[1]
		#Now we start top-tagging.  In this file, we use a sideband based on inverting some top-tagging requirements
		if tmass_cut:
			minmass_cut = minmass[0]<=topJetMinMass[0]<minmass[1]
			ht = tjet.pt() + wjet.pt()
			if options.trigger != "none" :
				#Trigger reweighting done here
				TRW = Trigger_Lookup( ht , TrigPlot , options.trigger )
				weight*=TRW



			if options.ptreweight == "on":
				#ttbar pt reweighting done here
				event.getByLabel( GenLabel, GenHandle )
				GenParticles = GenHandle.product()
				PTW = PTW_Lookup( GenParticles )
				weight*=PTW


    			event.getByLabel (TopBDiscsj0CSVLabel, TopBDiscsj0CSVHandle)
    			Topsj0BDiscCSV 		= 	TopBDiscsj0CSVHandle.product() 

    			event.getByLabel (TopBDiscsj1CSVLabel, TopBDiscsj1CSVHandle)
    			Topsj1BDiscCSV 		= 	TopBDiscsj1CSVHandle.product() 

    			event.getByLabel (TopBDiscsj2CSVLabel, TopBDiscsj2CSVHandle)
    			Topsj2BDiscCSV 		= 	TopBDiscsj2CSVHandle.product() 

    			event.getByLabel (TopBDiscsj3CSVLabel, TopBDiscsj3CSVHandle)
    			Topsj3BDiscCSV 		= 	TopBDiscsj3CSVHandle.product() 







    			event.getByLabel (CA8Label, CA8Handle)
    			CA8Jets 		= 	CA8Handle.product() 
	

    			event.getByLabel (TopTau3Label, TopTau3Handle)
    			Tau3		= 	TopTau3Handle.product() 


    			event.getByLabel (TopTau2Label, TopTau2Handle)
    			Tau2		= 	TopTau2Handle.product() 
		
    			event.getByLabel (TopTau1Label, TopTau1Handle)
    			Tau1		= 	TopTau1Handle.product() 

			index = -1

			for ijet in range(0,len(CA8Jets)):
				if (abs(ROOT.Math.VectorUtil.DeltaR(CA8Jets[ijet],wjet))<0.5):
					index = ijet
					break

			tau21val=Tau2[index]/Tau1[index]
			tau21_cut =  tau21[0]<=tau21val<tau21[1]


			index = -1
			for ijet in range(0,len(CA8Jets)):
				if (abs(ROOT.Math.VectorUtil.DeltaR(CA8Jets[ijet],tjet))<0.5):
					index = ijet
					break



			tau32val =  Tau3[index]/Tau2[index]
			tau32_cut =  tau32[0]<=tau32val<tau32[1]

			SJ_csvmax = max(Topsj0BDiscCSV[0],Topsj1BDiscCSV[0],Topsj2BDiscCSV[0],Topsj3BDiscCSV[0])
			sjbtag_cut = sjbtag[0]<SJ_csvmax<=sjbtag[1]
			wmass_cut = wmass[0][0]<=wjet.mass()<wmass[0][1] or wmass[1][0]<=wjet.mass()<wmass[1][1] 
			FullTop = sjbtag_cut and tau32_cut and nsubjets_cut and minmass_cut
			if wmass_cut:
				if tau21_cut:
					eta1_cut = eta1[0]<=abs(tjet.eta())<eta1[1]
					eta2_cut = eta2[0]<=abs(tjet.eta())<eta2[1]
					#Extract tags and probes for the average b tagging rate here 
					#We use three eta regions 
					if eta1_cut:
						MtwwptcomparepreSB1e1.Fill(tjet.pt(),(tjet+wjet).mass(),weight)
                				pteta1pretag.Fill( tjet.pt(),weight)
                				if FullTop :
							MtwwptcomparepostSB1e1.Fill(tjet.pt(),(tjet+wjet).mass(),weight)
                					pteta1.Fill( tjet.pt(),weight)
					if eta2_cut:
						MtwwptcomparepreSB1e2.Fill(tjet.pt(),(tjet+wjet).mass(),weight)
                				pteta2pretag.Fill( tjet.pt(),weight)
                				if FullTop :
							MtwwptcomparepostSB1e2.Fill(tjet.pt(),(tjet+wjet).mass(),weight)
                					pteta2.Fill( tjet.pt(),weight)
				
					temp_variables = {"wpt":wjet.pt(),"wmass":wjet.mass(),"tpt":tjet.pt(),"tmass":topJetMass[0],"tau32":tau32val,"tau21":tau21val,"nsubjets":NSubJets[0],"sjbtag":SJ_csvmax,"weight":weight}
					for tv in tree_vars.keys():
						tree_vars[tv][0] = temp_variables[tv]
					Tree.Fill()


f.cd()
f.Write()
f.Close()

print "number of events: " + str(count)
