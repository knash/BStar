
from optparse import OptionParser

from ROOT import *
import ROOT
gROOT.Macro("rootlogon.C")
nuisanceParams = {'bs1700': {'JER': [(0.094264200320780867, 0.80104617941701484)], 'JES': [(-0.99179927978746052, 0.55907141192989596)], 'flatUnc': [(-0.28409997988300095, 0.13070868973797409)], 'ttbar_rate': [(-0.83685017333456468, 0.29360806812424795)], '__nll': [-105029.75504901275], 'zjets_rate': [(0.62730859645573367, 0.74188789585858983)], 'wjets_rate': [(0.096211135618145358, 0.92381902606681043)], 'diBoson_rate': [(0.30807698443281101, 0.65121260722996377)], 'beta_signal': [(0.0, 5.5554437150763709)], 'lumi': [(-0.32233524072953068, 0.52475160129594489)], 'tW_rate': [(0.17833206835599283, 0.69514435685031017)]}, 'bs1800': {'JER': [(0.09000854123702326, 0.80008940360093561)], 'JES': [(-0.99571656194634506, 0.54983537167196961)], 'flatUnc': [(-0.28580515303566417, 0.13777727413747845)], 'ttbar_rate': [(-0.84078414949948843, 0.29483948031663626)], '__nll': [-105029.74970899586], 'zjets_rate': [(0.62874021414343351, 0.73798149023217574)], 'wjets_rate': [(0.095798549917788786, 0.92409591236548405)], 'diBoson_rate': [(0.31705687863598603, 0.65266271852473901)], 'beta_signal': [(0.0, 10.671257110472428)], 'lumi': [(-0.31887601202224319, 0.55489222496379431)], 'tW_rate': [(0.18889242234609946, 0.69721575746930076)]}, 'bs1300': {'JER': [(0.13334787596776293, 0.79688857264924662)], 'JES': [(-0.92781579819744309, 0.64108361584384532)], 'flatUnc': [(-0.40974375845214112, 0.3144494275725801)], 'ttbar_rate': [(-0.54667688532369596, 0.78769263226204633)], '__nll': [-105029.88621290681], 'zjets_rate': [(0.77977353468834409, 0.8521329892226035)], 'wjets_rate': [(0.0858708406453461, 0.9289562242658812)], 'diBoson_rate': [(0.20479888694320161, 0.61873290442439899)], 'beta_signal': [(0.0, 0.93874594310694792)], 'lumi': [(-0.014109298562076562, 0.86311141682007642)], 'tW_rate': [(0.097233614263555215, 0.92982790627749912)]}, 'bs1400': {'JER': [(0.13681644645115967, 0.80587430198650101)], 'JES': [(-0.89463182082105197, 0.63147313589045084)], 'flatUnc': [(-0.42508526249221157, 0.34093111806239812)], 'ttbar_rate': [(-0.46774351765571198, 0.94063428647665948)], '__nll': [-105029.8884779456], 'zjets_rate': [(0.79454239341306288, 0.83729977864531124)], 'wjets_rate': [(0.090214058825035276, 0.92496427060538522)], 'diBoson_rate': [(0.33472612511249517, 0.95228002415654112)], 'beta_signal': [(0.0, 1.5915068311714218)], 'lumi': [(-0.092210835176992356, 0.98416822393589709)], 'tW_rate': [(-0.0018857762767054975, 0.97178902901182984)]}, 'bs2000': {'JER': [(0.085362675257058776, 0.79566098000179253)], 'JES': [(-1.0109726774046073, 0.52886489850641294)], 'flatUnc': [(-0.28739226277535079, 0.14459334252017825)], 'ttbar_rate': [(-0.84247335172031157, 0.29570394399284994)], '__nll': [-105029.74851894735], 'zjets_rate': [(0.61823100209641746, 0.72572074021043642)], 'wjets_rate': [(0.095738824764870167, 0.92463755525553426)], 'diBoson_rate': [(0.32596108040200356, 0.65549812819649711)], 'beta_signal': [(0.0, 27.28335307714806)], 'lumi': [(-0.311606570709069, 0.58461814939151246)], 'tW_rate': [(0.19390395819491962, 0.69859565536268542)]}, 'bs1000': {'JER': [(0.10018577459904235, 0.80922832102884601)], 'JES': [(-0.87784449466221814, 0.42779447784141111)], 'flatUnc': [(-0.31573523617085003, -0.20487950691415638)], 'ttbar_rate': [(-0.74361585745934022, -0.87824940276815433)], '__nll': [-105029.82662714749], 'zjets_rate': [(0.61740708226055507, 0.82836856534128789)], 'wjets_rate': [(0.12580676508199171, 0.94577979403618517)], 'diBoson_rate': [(0.27126145374780941, -0.20701598659039813)], 'beta_signal': [(0.0, 0.26056134000770725)], 'lumi': [(-0.11102034916238063, 0.81630702169118219)], 'tW_rate': [(-0.07741921894943031, 0.55486472415097177)]}, 'bs1900': {'JER': [(0.084849293114617197, 0.7969784069695306)], 'JES': [(-1.0098805820802468, 0.53109637047167635)], 'flatUnc': [(-0.28701144413125307, 0.14446252490504394)], 'ttbar_rate': [(-0.8436682134981951, 0.2956300917868126)], '__nll': [-105029.74354422053], 'zjets_rate': [(0.62806647339946253, 0.7313878352023091)], 'wjets_rate': [(0.094796484712388593, 0.92447284300290511)], 'diBoson_rate': [(0.32457552154132124, 0.65459662330242518)], 'beta_signal': [(0.0, 17.643042110747274)], 'lumi': [(-0.31603700439568305, 0.58422106336449631)], 'tW_rate': [(0.19661017724795582, 0.69854027722402179)]}, 'bs1500': {'JER': [(0.13657283012422744, 0.80504191669087655)], 'JES': [(-0.90294620032337902, 0.60480307697933033)], 'flatUnc': [(-0.42690610410695035, 0.34090797171169401)], 'ttbar_rate': [(-0.46781845723346133, 0.93835834732324275)], '__nll': [-105029.88588939623], 'zjets_rate': [(0.78902749803925121, 0.81686856031412525)], 'wjets_rate': [(0.087556095890832172, 0.92284862115882971)], 'diBoson_rate': [(0.36749768897264956, 0.9467094241514632)], 'beta_signal': [(0.0, 2.6496675950301856)], 'lumi': [(-0.094067892654069174, 0.98109116754562142)], 'tW_rate': [(-0.01245503532263182, 0.97395346215405509)]}, 'bs900': {'JER': [(0.12333851313788916, 0.80025999528822955)], 'JES': [(-0.91293235139085327, 0.66446060570531185)], 'flatUnc': [(-0.29101232754514611, 0.13403804056320015)], 'ttbar_rate': [(-0.81217401360631869, -0.21218853119121758)], '__nll': [-105029.77591500161], 'zjets_rate': [(0.6133613024941531, 0.45165780871565558)], 'wjets_rate': [(0.10122048943086444, 0.82557589812818888)], 'diBoson_rate': [(0.32195367244445633, 0.48635731168399854)], 'beta_signal': [(0.0, 0.15295771874022779)], 'lumi': [(-0.26401230470221493, 0.29761441138407152)], 'tW_rate': [(0.10733556511575516, 0.49296137701562853)]}, 'bs1100': {'JER': [(0.11871229887303399, 0.81449116539409983)], 'JES': [(-0.86752051376274553, 0.39811718750936997)], 'flatUnc': [(-0.32742777551814345, -0.24484867129947782)], 'ttbar_rate': [(-0.75896169108119726, -0.94943303982257832)], '__nll': [-105029.81769817598], 'zjets_rate': [(0.7178236200158159, 0.82979463261919595)], 'wjets_rate': [(0.066625800895257978, 0.8992941013394965)], 'diBoson_rate': [(0.29435354773878991, -0.50655917934290251)], 'beta_signal': [(0.0, 0.34612406981221205)], 'lumi': [(-0.12151064718817427, 0.83723063007349363)], 'tW_rate': [(-0.017876769861563793, 0.47364716283078589)]}, 'bs1600': {'JER': [(-0.057391418839519093, 0.80158981906181759)], 'JES': [(-0.97263933718980189, 0.56933464931894551)], 'flatUnc': [(-0.21266689840120889, 0.12205627136119979)], 'ttbar_rate': [(-0.75905117407478873, 0.31363398744716692)], '__nll': [-105029.43704866711], 'zjets_rate': [(0.8421739031320945, 0.78339654116582613)], 'wjets_rate': [(0.14023141379336118, 0.92471817485793484)], 'diBoson_rate': [(0.072963101671921035, 0.57942816040270217)], 'beta_signal': [(0.0, 10.763346676307439)], 'lumi': [(-0.59144898418504432, 0.48833281235634984)], 'tW_rate': [(0.063929603163160764, 0.75341911278740936)]}, 'bs800': {'JER': [(0.11056918314070222, 0.79522018123574822)], 'JES': [(-0.97971871456960535, 0.63858714737317501)], 'flatUnc': [(-0.31409930199306541, 0.14808258918143352)], 'ttbar_rate': [(-0.73054750692922199, 0.34750868608794838)], '__nll': [-105029.85362758636], 'zjets_rate': [(0.59233946065820153, 0.80312731222030287)], 'wjets_rate': [(0.08448635160145436, 0.93359169225851857)], 'diBoson_rate': [(0.27732807377018998, 0.64049486190039706)], 'beta_signal': [(0.0, 0.099679627085609041)], 'lumi': [(-0.16775769247744374, 0.88216266719619518)], 'tW_rate': [(-0.016640258138502811, 0.79308540172729913)]}, 'bs1200': {'JER': [(0.11032672804136825, 0.80587027249374932)], 'JES': [(-1.0268850429028511, 0.57080594635991866)], 'flatUnc': [(-0.27947262023025243, 0.13641570252332746)], 'ttbar_rate': [(-0.81744609520270783, 0.2996750205532886)], '__nll': [-105029.77959597285], 'zjets_rate': [(0.56138596449135647, 0.77797336676990658)], 'wjets_rate': [(0.15745959861597181, 0.93004129805739089)], 'diBoson_rate': [(0.28991210914152232, 0.65775536925948919)], 'beta_signal': [(0.0, 0.57733573418262907)], 'lumi': [(-0.30926498400711078, 0.54184026802773722)], 'tW_rate': [(0.12704833316799238, 0.66863299064301795)]}}
covl = ['BTag', 'JER', 'JES', 'Mass', 'MisTag', 'PDF', 'PU', 'Q2', 'QCD_rate_El', 'QCD_rate_Mu', 'UnclusteredMET', 'beta_signal', 'bkg', 'diBoson_rate', 'flatUnc', 'leptonSFID', 'leptonSFIso', 'leptonSFTrig', 'lumi', 'schannel_rate', 'subjet_scalefactor', 'tW_rate', 'tau_scalefactor', 'tchannel_rate', 'trig', 'ttbar_rate', 'ttbar_rate_had', 'wjets_rate', 'wjets_rate_El', 'wjets_rate_Mu', 'zjets_rate']
cov = [[  9.49329174e-01,   1.48108338e-03,   1.79879135e-03,
          2.20783695e-03,   1.45534576e-02,  -1.24288319e-01,
          3.47843689e-02,   5.78095575e-03,   4.20936773e-02,
          2.46281098e-02,   1.56247158e-02,   1.10967177e-03,
          2.59763288e-04,  -6.56196841e-03,   3.96926452e-02,
         -3.90899503e-02,  -6.63544456e-03,  -2.55843701e-02,
         -5.03548325e-02,  -1.65334001e-05,  -2.69304047e-03,
         -4.92223262e-02,  -3.30946358e-03,   1.89008370e-03,
          1.10800923e-05,  -9.12663492e-02,  -5.12609801e-03,
          2.69592382e-04,  -2.65652286e-01,  -1.37442966e-01,
         -3.06900671e-02],
       [  1.48108338e-03,   3.37476664e-02,  -9.77627937e-03,
         -1.26764735e-03,   1.17202448e-03,  -5.79940063e-03,
          2.30415389e-02,   1.41889330e-03,  -9.01699914e-04,
          5.26578227e-03,   1.96811377e-02,  -2.78066318e-03,
          4.98368589e-03,   1.07273568e-02,  -1.31295711e-02,
         -1.44030494e-03,  -2.24829387e-04,  -7.49071756e-04,
          1.03086085e-03,  -5.40260560e-05,   2.94064775e-03,
         -7.60653653e-03,   4.73349580e-03,  -8.01392051e-04,
         -2.77111648e-05,   1.97747791e-02,   8.37160299e-03,
         -1.97590452e-02,  -1.85750470e-03,   3.81211997e-03,
         -4.46927031e-02],
       [  1.79879135e-03,  -9.77627937e-03,   8.70611499e-02,
          3.53842227e-02,   1.81321884e-03,  -3.36879034e-03,
          3.58782898e-02,  -3.47509327e-03,  -1.15514366e-02,
         -1.39858240e-02,  -3.05022396e-02,  -1.40293255e-02,
         -3.54633303e-03,   7.34630797e-05,  -7.59530992e-03,
         -3.41609074e-03,  -3.81925002e-04,  -2.29709506e-03,
          1.64833424e-03,   1.02605591e-06,   8.47496939e-03,
          2.35705982e-03,   5.81063588e-03,   3.56555985e-03,
         -1.56365707e-04,  -1.35402234e-02,  -1.00687665e-03,
         -1.21772334e-02,  -6.43519485e-03,   4.96522610e-03,
          4.83584567e-02],
       [  2.20783695e-03,  -1.26764735e-03,   3.53842227e-02,
          7.40756434e-01,   8.39892583e-03,  -8.39889323e-02,
          4.27815145e-02,  -3.65650020e-02,  -1.09949141e-02,
          1.09431182e-02,  -8.23956100e-02,  -2.50066072e-03,
         -1.17337482e-03,   2.86024719e-04,   3.48040367e-04,
         -1.26919467e-02,  -1.41113947e-03,  -7.85447733e-03,
         -5.47978852e-03,  -8.08191141e-04,   3.36739236e-03,
          5.67904530e-03,   1.02845294e-02,   6.30294288e-03,
         -6.48853342e-07,  -1.82001510e-02,   2.45231220e-02,
         -7.00935562e-03,  -3.33529472e-02,   1.24205074e-02,
          1.05089404e-02],
       [  1.45534576e-02,   1.17202448e-03,   1.81321884e-03,
          8.39892583e-03,   5.75630360e-01,  -5.39562797e-02,
         -1.33536302e-02,   4.68319274e-03,   1.86014591e-02,
         -3.33973901e-02,   1.31099113e-03,  -3.16868178e-03,
          1.85918593e-03,   2.69343264e-03,  -9.12185154e-03,
         -4.34183685e-03,  -9.71934120e-04,  -2.13990322e-03,
          1.08461473e-02,   1.01784193e-04,   2.52532335e-03,
          1.06152487e-02,   1.77383217e-03,   1.19479690e-03,
         -3.60542967e-05,   1.95603869e-02,   1.49058204e-04,
         -6.96434266e-04,  -1.02979330e-01,  -2.02137528e-02,
          2.29111324e-03],
       [ -1.24288319e-01,  -5.79940063e-03,  -3.36879034e-03,
         -8.39889323e-02,  -5.39562797e-02,   3.65428381e-01,
          1.62167338e-02,  -1.14056056e-02,  -1.21035705e-01,
         -1.83048352e-01,  -3.12855797e-02,  -1.84456813e-03,
          8.28405971e-03,  -2.87018650e-02,   7.58945009e-02,
         -6.93746964e-02,  -9.17680495e-03,  -5.67029791e-02,
         -9.14793075e-02,  -2.96528731e-03,  -8.83633900e-05,
         -9.04266674e-02,   5.79727544e-03,  -1.89888835e-02,
          1.19948668e-05,  -1.66285701e-01,   1.70511904e-02,
          6.25611128e-03,   2.36311211e-01,  -2.88084992e-01,
         -2.02246730e-02],
       [  3.47843689e-02,   2.30415389e-02,   3.58782898e-02,
          4.27815145e-02,  -1.33536302e-02,   1.62167338e-02,
          8.23174322e-01,   3.08734742e-02,  -6.97373069e-02,
         -1.09881752e-01,   4.88357694e-02,  -1.28831240e-02,
          1.74778893e-03,   8.93123807e-03,  -2.37400751e-02,
         -1.16876534e-03,   2.96944402e-04,   5.84175614e-04,
          1.20331431e-02,  -1.22792781e-03,   7.92931119e-03,
          1.39413254e-02,   5.79662887e-04,  -4.91507378e-03,
         -1.67691058e-04,   2.68132911e-02,  -1.55562897e-02,
         -2.28179865e-02,  -1.66635207e-02,   2.87864147e-02,
         -1.46231098e-03],
       [  5.78095575e-03,   1.41889330e-03,  -3.47509327e-03,
         -3.65650020e-02,   4.68319274e-03,  -1.14056056e-02,
          3.08734742e-02,   3.31207208e-02,   7.48711844e-03,
         -1.37673402e-02,   2.45318861e-02,  -1.59276709e-03,
         -1.55465467e-03,   5.08453804e-03,  -1.11577401e-02,
          2.11446704e-03,   5.17062836e-04,   1.89238975e-03,
          1.38463086e-02,  -3.78663545e-06,  -6.02233017e-04,
          7.33635094e-03,  -8.46847968e-03,  -4.69828561e-04,
         -4.76580430e-05,   2.72180786e-02,  -2.49608952e-02,
         -2.98533542e-04,  -3.06995535e-02,   1.28558685e-02,
          3.65978492e-03],
       [  4.20936773e-02,  -9.01699914e-04,  -1.15514366e-02,
         -1.09949141e-02,   1.86014591e-02,  -1.21035705e-01,
         -6.97373069e-02,   7.48711844e-03,   5.69379925e-01,
          8.14569861e-02,  -5.12377425e-02,  -2.34852661e-03,
          1.60723340e-03,  -6.45326182e-03,  -3.07765151e-02,
          1.55574089e-02,   2.15633704e-03,   1.14439258e-02,
          4.02007970e-02,  -1.61960553e-03,   3.24375537e-03,
          5.27399479e-02,   1.58903659e-03,  -1.17131788e-02,
         -3.18721096e-05,   7.35595868e-02,  -1.34865190e-03,
          2.04266842e-03,  -2.94350053e-01,   7.13639482e-02,
          2.83586918e-02],
       [  2.46281098e-02,   5.26578227e-03,  -1.39858240e-02,
          1.09431182e-02,  -3.33973901e-02,  -1.83048352e-01,
         -1.09881752e-01,  -1.37673402e-02,   8.14569861e-02,
          7.09673547e-01,  -5.68595500e-02,  -9.45775521e-03,
          1.07463572e-02,   1.57881967e-02,  -5.35447787e-02,
          4.24827454e-03,   3.50540244e-03,  -1.07573717e-02,
          6.32846367e-02,  -2.66176486e-03,   1.13005897e-02,
          7.17651850e-02,   1.66791328e-02,  -2.22631785e-02,
         -7.79900976e-05,   1.29920895e-01,   2.84112175e-02,
          2.70885029e-03,  -1.17306958e-01,  -1.81113923e-01,
         -5.25940766e-03],
       [  1.56247158e-02,   1.96811377e-02,  -3.05022396e-02,
         -8.23956100e-02,   1.31099113e-03,  -3.12855797e-02,
          4.88357694e-02,   2.45318861e-02,  -5.12377425e-02,
         -5.68595500e-02,   6.89238952e-01,   1.36475915e-03,
          2.30903164e-03,   8.02056735e-03,  -5.12941537e-03,
          1.62812041e-03,   9.70179229e-04,   1.71797767e-03,
         -9.43850356e-04,  -1.72826418e-03,  -1.30506724e-03,
          1.55561884e-03,  -5.15929803e-03,  -1.00899445e-02,
         -3.59199493e-06,   1.35827518e-02,  -1.29748708e-02,
         -6.22207898e-03,   1.36115350e-02,   1.05357961e-01,
         -3.60627692e-02],
       [  1.10967177e-03,  -2.78066318e-03,  -1.40293255e-02,
         -2.50066072e-03,  -3.16868178e-03,  -1.84456813e-03,
         -1.28831240e-02,  -1.59276709e-03,  -2.34852661e-03,
         -9.45775521e-03,   1.36475915e-03,   2.68926196e-02,
         -2.42815711e-02,  -4.18304925e-03,   2.57165232e-03,
          3.01783739e-03,   3.87972210e-04,   1.84783430e-03,
         -2.28930186e-03,   7.45827052e-07,  -2.17187823e-02,
         -6.15181070e-03,  -2.71733233e-02,  -1.39095971e-04,
          2.52368296e-04,   6.71555795e-03,  -3.72801421e-02,
          7.67906487e-04,  -2.09280259e-04,   1.08721404e-03,
         -5.07027886e-03],
       [  2.59763288e-04,   4.98368589e-03,  -3.54633303e-03,
         -1.17337482e-03,   1.85918593e-03,   8.28405971e-03,
          1.74778893e-03,  -1.55465467e-03,   1.60723340e-03,
          1.07463572e-02,   2.30903164e-03,  -2.42815711e-02,
          2.09378181e-01,   4.60989415e-03,   4.12333099e-03,
         -8.89232511e-04,  -9.35115894e-05,  -4.73729673e-04,
         -3.30900316e-03,   9.98258952e-08,  -1.46411188e-02,
         -4.07929296e-02,  -7.62860635e-02,  -3.34745098e-03,
         -9.95910877e-04,  -1.81628617e-03,  -2.01004218e-01,
          1.61285934e-03,   1.23881909e-02,  -7.02078923e-04,
         -3.80906699e-03],
       [ -6.56196841e-03,   1.07273568e-02,   7.34630797e-05,
          2.86024719e-04,   2.69343264e-03,  -2.87018650e-02,
          8.93123807e-03,   5.08453804e-03,  -6.45326182e-03,
          1.57881967e-02,   8.02056735e-03,  -4.18304925e-03,
          4.60989415e-03,   1.17117047e+00,  -1.74036722e-01,
         -9.19458213e-03,  -1.46153787e-03,  -5.54031619e-03,
         -2.90284712e-02,  -9.05159991e-05,   2.79897005e-03,
         -1.62747535e-02,   3.22018798e-03,  -8.28844725e-04,
         -4.21333430e-05,   1.22274537e-01,   3.69783733e-03,
         -3.94104687e-02,  -3.28023080e-02,  -1.10856209e-02,
         -3.21019378e-01],
       [  3.96926452e-02,  -1.31295711e-02,  -7.59530992e-03,
          3.48040367e-04,  -9.12185154e-03,   7.58945009e-02,
         -2.37400751e-02,  -1.11577401e-02,  -3.07765151e-02,
         -5.35447787e-02,  -5.12941537e-03,   2.57165232e-03,
          4.12333099e-03,  -1.74036722e-01,   1.09525160e-01,
          3.30613453e-02,   5.10135422e-03,   2.19783317e-02,
         -1.04246553e-01,   9.88312668e-05,  -3.44933553e-03,
         -7.71887654e-02,   1.20257264e-03,  -2.60626147e-03,
          5.24844522e-05,  -1.91030416e-01,   1.02174904e-02,
          8.27024781e-03,   1.22930889e-01,   3.88086146e-02,
         -6.58908401e-03],
       [ -3.90899503e-02,  -1.44030494e-03,  -3.41609074e-03,
         -1.26919467e-02,  -4.34183685e-03,  -6.93746964e-02,
         -1.16876534e-03,   2.11446704e-03,   1.55574089e-02,
          4.24827454e-03,   1.62812041e-03,   3.01783739e-03,
         -8.89232511e-04,  -9.19458213e-03,   3.30613453e-02,
          9.63791444e-01,  -6.15998229e-03,  -2.78066504e-02,
         -4.01445445e-02,  -5.87920081e-04,  -3.47993595e-03,
         -3.45436309e-02,  -3.64994716e-03,   1.11040312e-04,
          3.23994377e-05,  -7.45468165e-02,  -4.24188070e-03,
          2.16891655e-03,   2.27165068e-02,  -9.17015825e-02,
         -1.69814450e-02],
       [ -6.63544456e-03,  -2.24829387e-04,  -3.81925002e-04,
         -1.41113947e-03,  -9.71934120e-04,  -9.17680495e-03,
          2.96944402e-04,   5.17062836e-04,   2.15633704e-03,
          3.50540244e-03,   9.70179229e-04,   3.87972210e-04,
         -9.35115894e-05,  -1.46153787e-03,   5.10135422e-03,
         -6.15998229e-03,   1.01040386e+00,  -4.14667940e-03,
         -6.18293329e-03,  -8.03156686e-05,  -5.00071297e-04,
         -5.68193803e-03,  -5.58135268e-04,   1.06499427e-06,
          4.09886552e-06,  -1.14449532e-02,  -7.24596567e-04,
          3.09885572e-04,   7.83382641e-03,  -1.41401944e-02,
         -2.45796530e-03],
       [ -2.55843701e-02,  -7.49071756e-04,  -2.29709506e-03,
         -7.85447733e-03,  -2.13990322e-03,  -5.67029791e-02,
          5.84175614e-04,   1.89238975e-03,   1.14439258e-02,
         -1.07573717e-02,   1.71797767e-03,   1.84783430e-03,
         -4.73729673e-04,  -5.54031619e-03,   2.19783317e-02,
         -2.78066504e-02,  -4.14667940e-03,   9.84223334e-01,
         -2.68736879e-02,  -3.59663194e-04,  -2.21195355e-03,
         -2.29494491e-02,  -2.40094560e-03,  -6.80458287e-05,
          1.95952405e-05,  -4.97811208e-02,  -2.96181206e-03,
          1.36547574e-03,  -7.70565175e-03,  -5.95877266e-02,
         -1.21154974e-02],
       [ -5.03548325e-02,   1.03086085e-03,   1.64833424e-03,
         -5.47978852e-03,   1.08461473e-02,  -9.14793075e-02,
          1.20331431e-02,   1.38463086e-02,   4.02007970e-02,
          6.32846367e-02,  -9.43850356e-04,  -2.28930186e-03,
         -3.30900316e-03,  -2.90284712e-02,  -1.04246553e-01,
         -4.01445445e-02,  -6.18293329e-03,  -2.68736879e-02,
          9.18783368e-01,  -3.32123898e-04,   1.57517529e-03,
         -7.19532373e-02,  -3.12570486e-03,   1.67760456e-03,
         -3.98321638e-05,  -1.46187276e-01,  -1.24235891e-02,
          8.03229533e-04,  -1.52556182e-01,  -5.02500051e-02,
         -3.75727757e-02],
       [ -1.65334001e-05,  -5.40260560e-05,   1.02605591e-06,
         -8.08191141e-04,   1.01784193e-04,  -2.96528731e-03,
         -1.22792781e-03,  -3.78663545e-06,  -1.61960553e-03,
         -2.66176486e-03,  -1.72826418e-03,   7.45827052e-07,
          9.98258952e-08,  -9.05159991e-05,   9.88312668e-05,
         -5.87920081e-04,  -8.03156686e-05,  -3.59663194e-04,
         -3.32123898e-04,   9.99012530e-01,  -7.65919072e-07,
          5.21163658e-05,  -7.87573464e-07,  -8.57464234e-05,
          2.05439378e-08,  -1.01002277e-04,  -8.38481956e-07,
          3.21730282e-05,  -4.10894599e-03,  -2.38557752e-04,
          1.25208283e-04],
       [ -2.69304047e-03,   2.94064775e-03,   8.47496939e-03,
          3.36739236e-03,   2.52532335e-03,  -8.83633900e-05,
          7.92931119e-03,  -6.02233017e-04,   3.24375537e-03,
          1.13005897e-02,  -1.30506724e-03,  -2.17187823e-02,
         -1.46411188e-02,   2.79897005e-03,  -3.44933553e-03,
         -3.47993595e-03,  -5.00071297e-04,  -2.21195355e-03,
          1.57517529e-03,  -7.65919072e-07,   1.03233569e+00,
          3.16539016e-02,   1.86178464e-02,  -1.68434805e-03,
         -2.82785962e-04,  -9.41883572e-03,   4.24590957e-04,
         -3.59636532e-04,  -1.65350790e-03,  -3.49720944e-03,
          6.06565342e-04],
       [ -4.92223262e-02,  -7.60653653e-03,   2.35705982e-03,
          5.67904530e-03,   1.06152487e-02,  -9.04266674e-02,
          1.39413254e-02,   7.33635094e-03,   5.27399479e-02,
          7.17651850e-02,   1.55561884e-03,  -6.15181070e-03,
         -4.07929296e-02,  -1.62747535e-02,  -7.71887654e-02,
         -3.45436309e-02,  -5.68193803e-03,  -2.29494491e-02,
         -7.19532373e-02,   5.21163658e-05,   3.16539016e-02,
          1.12608571e+00,   6.55924631e-03,   2.30338794e-03,
         -2.22075983e-04,  -1.00151278e-01,  -3.54343330e-02,
          5.51339597e-03,  -1.54675762e-01,  -5.98049301e-02,
         -2.73827276e-02],
       [ -3.30946358e-03,   4.73349580e-03,   5.81063588e-03,
          1.02845294e-02,   1.77383217e-03,   5.79727544e-03,
          5.79662887e-04,  -8.46847968e-03,   1.58903659e-03,
          1.66791328e-02,  -5.15929803e-03,  -2.71733233e-02,
         -7.62860635e-02,   3.22018798e-03,   1.20257264e-03,
         -3.64994716e-03,  -5.58135268e-04,  -2.40094560e-03,
         -3.12570486e-03,  -7.87573464e-07,   1.86178464e-02,
          6.55924631e-03,   1.00577291e+00,  -1.94856938e-03,
         -1.59692218e-03,  -1.39805187e-02,  -5.31150343e-02,
          1.05580182e-04,   1.06164170e-02,  -5.88889989e-03,
         -2.77326938e-03],
       [  1.89008370e-03,  -8.01392051e-04,   3.56555985e-03,
          6.30294288e-03,   1.19479690e-03,  -1.89888835e-02,
         -4.91507378e-03,  -4.69828561e-04,  -1.17131788e-02,
         -2.22631785e-02,  -1.00899445e-02,  -1.39095971e-04,
         -3.34745098e-03,  -8.28844725e-04,  -2.60626147e-03,
          1.11040312e-04,   1.06499427e-06,  -6.80458287e-05,
          1.67760456e-03,  -8.57464234e-05,  -1.68434805e-03,
          2.30338794e-03,  -1.94856938e-03,   9.93115490e-01,
         -3.71298017e-05,   6.25077173e-03,  -2.43969032e-03,
         -5.16101102e-04,  -2.13458948e-02,   1.71679497e-03,
          5.93549213e-03],
       [  1.10800923e-05,  -2.77111648e-05,  -1.56365707e-04,
         -6.48853342e-07,  -3.60542967e-05,   1.19948668e-05,
         -1.67691058e-04,  -4.76580430e-05,  -3.18721096e-05,
         -7.79900976e-05,  -3.59199493e-06,   2.52368296e-04,
         -9.95910877e-04,  -4.21333430e-05,   5.24844522e-05,
          3.23994377e-05,   4.09886552e-06,   1.95952405e-05,
         -3.98321638e-05,   2.05439378e-08,  -2.82785962e-04,
         -2.22075983e-04,  -1.59692218e-03,  -3.71298017e-05,
          1.00086731e+00,   5.18811968e-05,  -4.27316377e-03,
          1.47089518e-05,   5.67897240e-05,   3.68479259e-06,
         -5.62360881e-05],
       [ -9.12663492e-02,   1.97747791e-02,  -1.35402234e-02,
         -1.82001510e-02,   1.95603869e-02,  -1.66285701e-01,
          2.68132911e-02,   2.72180786e-02,   7.35595868e-02,
          1.29920895e-01,   1.35827518e-02,   6.71555795e-03,
         -1.81628617e-03,   1.22274537e-01,  -1.91030416e-01,
         -7.45468165e-02,  -1.14449532e-02,  -4.97811208e-02,
         -1.46187276e-01,  -1.01002277e-04,  -9.41883572e-03,
         -1.00151278e-01,  -1.39805187e-02,   6.25077173e-03,
          5.18811968e-05,   7.75848061e-01,  -2.43552766e-02,
         -1.18059216e-02,  -2.70199373e-01,  -8.90709251e-02,
          7.37814341e-02],
       [ -5.12609801e-03,   8.37160299e-03,  -1.00687665e-03,
          2.45231220e-02,   1.49058204e-04,   1.70511904e-02,
         -1.55562897e-02,  -2.49608952e-02,  -1.34865190e-03,
          2.84112175e-02,  -1.29748708e-02,  -3.72801421e-02,
         -2.01004218e-01,   3.69783733e-03,   1.02174904e-02,
         -4.24188070e-03,  -7.24596567e-04,  -2.96181206e-03,
         -1.24235891e-02,  -8.38481956e-07,   4.24590957e-04,
         -3.54343330e-02,  -5.31150343e-02,  -2.43969032e-03,
         -4.27316377e-03,  -2.43552766e-02,   9.32036161e-01,
          1.24043402e-03,   3.46569661e-02,  -1.15603000e-02,
         -1.07865207e-02],
       [  2.69592382e-04,  -1.97590452e-02,  -1.21772334e-02,
         -7.00935562e-03,  -6.96434266e-04,   6.25611128e-03,
         -2.28179865e-02,  -2.98533542e-04,   2.04266842e-03,
          2.70885029e-03,  -6.22207898e-03,   7.67906487e-04,
          1.61285934e-03,  -3.94104687e-02,   8.27024781e-03,
          2.16891655e-03,   3.09885572e-04,   1.36547574e-03,
          8.03229533e-04,   3.21730282e-05,  -3.59636532e-04,
          5.51339597e-03,   1.05580182e-04,  -5.16101102e-04,
          1.47089518e-05,  -1.18059216e-02,   1.24043402e-03,
          1.13820079e+00,   6.99183902e-03,  -3.24932987e-03,
         -3.24935928e-02],
       [ -2.65652286e-01,  -1.85750470e-03,  -6.43519485e-03,
         -3.33529472e-02,  -1.02979330e-01,   2.36311211e-01,
         -1.66635207e-02,  -3.06995535e-02,  -2.94350053e-01,
         -1.17306958e-01,   1.36115350e-02,  -2.09280259e-04,
          1.23881909e-02,  -3.28023080e-02,   1.22930889e-01,
          2.27165068e-02,   7.83382641e-03,  -7.70565175e-03,
         -1.52556182e-01,  -4.10894599e-03,  -1.65350790e-03,
         -1.54675762e-01,   1.06164170e-02,  -2.13458948e-02,
          5.67897240e-05,  -2.70199373e-01,   3.46569661e-02,
          6.99183902e-03,   4.74082777e-01,   5.18931117e-02,
         -6.81423680e-02],
       [ -1.37442966e-01,   3.81211997e-03,   4.96522610e-03,
          1.24205074e-02,  -2.02137528e-02,  -2.88084992e-01,
          2.87864147e-02,   1.28558685e-02,   7.13639482e-02,
         -1.81113923e-01,   1.05357961e-01,   1.08721404e-03,
         -7.02078923e-04,  -1.10856209e-02,   3.88086146e-02,
         -9.17015825e-02,  -1.41401944e-02,  -5.95877266e-02,
         -5.02500051e-02,  -2.38557752e-04,  -3.49720944e-03,
         -5.98049301e-02,  -5.88889989e-03,   1.71679497e-03,
          3.68479259e-06,  -8.90709251e-02,  -1.15603000e-02,
         -3.24932987e-03,   5.18931117e-02,   1.01079397e+00,
         -1.87228393e-02],
       [ -3.06900671e-02,  -4.46927031e-02,   4.83584567e-02,
          1.05089404e-02,   2.29111324e-03,  -2.02246730e-02,
         -1.46231098e-03,   3.65978492e-03,   2.83586918e-02,
         -5.25940766e-03,  -3.60627692e-02,  -5.07027886e-03,
         -3.80906699e-03,  -3.21019378e-01,  -6.58908401e-03,
         -1.69814450e-02,  -2.45796530e-03,  -1.21154974e-02,
         -3.75727757e-02,   1.25208283e-04,   6.06565342e-04,
         -2.73827276e-02,  -2.77326938e-03,   5.93549213e-03,
         -5.62360881e-05,   7.37814341e-02,  -1.07865207e-02,
         -3.24935928e-02,  -6.81423680e-02,  -1.87228393e-02,
          7.02987022e-01]]

Covplot = ROOT.TH2F("Covplot",     "nuisanceplot",     	  	len(covl), -0.5, len(covl)+0.5 ,len(covl), -0.5, len(covl)+0.5)
for xbin in range(1,Covplot.GetXaxis().GetNbins()):
	for ybin in range(1,Covplot.GetYaxis().GetNbins()):
		if xbin == 0:
			Covplot.GetXaxis().SetBinLabel(ybin, str(covl[ybin]))
			Covplot.GetYaxis().SetBinLabel(ybin, str(covl[ybin]))
		Covplot.SetBinContent(xbin,ybin,float(cov[xbin][ybin]))
c2 = TCanvas('c2', 'cov', 2000, 2000)
Covplot.Draw("colz")
c2.Print('Covtemp.root', 'root')
c2.Print('Covtemp.pdf', 'pdf')


c1 = TCanvas('c1', 'NP', 1200, 350)
for iset in nuisanceParams:
	NPplot = ROOT.TH1F("NPplot",     "nuisanceplot",     	  	len(nuisanceParams[iset])-1, -0.5, len(nuisanceParams[iset])-0.5 )
	S95low  = TLine(-0.5,-2,len(nuisanceParams[iset])-0.5,-2)
	S95high = TLine(-0.5,2,len(nuisanceParams[iset])-0.5,2)
	S68low = TLine(-0.5,-1,len(nuisanceParams[iset])-0.5,-1)
	S68high = TLine(-0.5,1,len(nuisanceParams[iset])-0.5,1)
	i = 0
   	for ipar in nuisanceParams[iset]:
		if str(ipar)!='beta_signal' and str(ipar)!='__nll' :
			i+=1
			NPplot.GetXaxis().SetBinLabel(i, str(ipar))
			NPplot.SetBinContent(i, nuisanceParams[iset][ipar][0][0])
			NPplot.SetBinError(i, nuisanceParams[iset][ipar][0][1])

	NPplot.SetTitle(';Nuisance Parameter;\sigma')
	NPplot.SetStats(0)
	NPplot.SetLineColor(1)
	NPplot.SetMarkerStyle(21)
	S95low.SetLineWidth(4)
	S95high.SetLineWidth(4)
	S68low.SetLineWidth(4)
	S68high.SetLineWidth(4)
	S95low.SetLineColor(5)
	S95high.SetLineColor(5)
	S68low.SetLineColor(3)
	S68high.SetLineColor(3)
	NPplot.GetXaxis().SetTickLength(0.0)

	NPplot.GetYaxis().SetRangeUser(-4,4)
	NPplot.GetXaxis().SetTitleOffset(1.2)
	NPplot.GetYaxis().SetTitleOffset(0.4)
	gPad.SetLeftMargin(0.06)
	gPad.SetRightMargin(0.06)
	gPad.SetBottomMargin(0.21)
	NPplot.Draw()
	S95low.Draw()
	S95high.Draw()
	S68low.Draw()
	S68high.Draw()
	NPplot.Draw("same")
        prelim = ROOT.TLatex()
        prelim.SetTextFont(42)
        prelim.SetNDC()
	prelim.DrawLatex( 0.15, 0.91, "#scale[1.0]{CMS Preliminary #sqrt{s} = 8 TeV}" )
	gPad.RedrawAxis()
	c1.Print('nuisanceright'+iset+'temp.root', 'root')
	c1.Print('nuisanceright'+iset+'temp.pdf', 'pdf')
