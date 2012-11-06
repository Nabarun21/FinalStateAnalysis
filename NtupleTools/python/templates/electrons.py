'''

Ntuple branch template sets for electron objects.

Each string is transformed into an expression on a FinalStateEvent object.

{object} should be replaced by an expression which evaluates to a pat::Electron
i.e. daughter(1) or somesuch.

Author: Evan K. Friis

'''

import FWCore.ParameterSet.Config as cms
from FinalStateAnalysis.Utilities.cfgtools import PSet

# ID and isolation
id = PSet(
    objectWWID = '{object}.userFloat("WWID")',
    objectMITID = '{object}.userFloat("MITID")',
    objectMVANonTrig = '{object}.electronID("mvaNonTrigV0")',
    objectMVATrig = '{object}.electronID("mvaTrigV0")',
    objectMVAIDH2TauWP = '{object}.userInt("mvaidwp")',
    objectCiCTight = '{object}.electronID("cicTight")',
    objectCBID_VETO = '{object}.userInt("CBID_VETO")',
    objectCBID_LOOSE = '{object}.userInt("CBID_LOOSE")',
    objectCBID_MEDIUM = '{object}.userInt("CBID_MEDIUM")',
    objectCBID_TIGHT = '{object}.userInt("CBID_TIGHT")',
    # Use cms.string so we get the parentheses formatting bonus
    objectRelPFIsoDB = cms.string(
        "({object}.userIso(0)"
        "+max({object}.userIso(1)"
        "+{object}.neutralHadronIso()"
        "-0.5*{object}.userIso(2),0.0))"
        "/{object}.pt()"
    ),
    objectPFChargedIso = cms.string('{object}.userIsolation(4)'),
    objectPFNeutralIso = cms.string('{object}.userIsolation(5)'),
    objectPFPhotonIso  = cms.string('{object}.userIsolation(6)'),
    objectEffectiveArea2012Data = cms.string('{object}.userFloat("ea_comb_Data2012_iso04_kt6PFJ")'),
    objectEffectiveArea2011Data = cms.string('{object}.userFloat("ea_comb_Data2011_iso04_kt6PFJ")'),
    objectEffectiveAreaFall11MC = cms.string('{object}.userFloat("ea_comb_Fall11MC_iso04_kt6PFJ")'),
    objectRelIso = cms.string("({object}.dr03TkSumPt()"
               "+max({object}.dr03EcalRecHitSumEt()-1.0,0.0)"
               "+{object}.dr03HcalTowerSumEt())/{object}.pt()"),
    objectChargeIdTight = '{object}.isGsfCtfScPixChargeConsistent',
    objectChargeIdMed = '{object}.isGsfScPixChargeConsistent',
    objectChargeIdLoose = '{object}.isGsfCtfChargeConsistent',
    # shower shape / ID variables
    objectHadronicOverEM = '{object}.hcalOverEcal',
    objectHadronicDepth1OverEm = '{object}.hadronicDepth1OverEcal',
    objectHadronicDepth2OverEm = '{object}.hadronicDepth2OverEcal',
    objectSigmaIEtaIEta = '{object}.sigmaIetaIeta',
    objectE1x5 = '{object}.scE1x5',
    objectE2x5 = '{object}.scE2x5',
    objectE2x5Max = '{object}.scE2x5Max',
    objectE5x5 = '{object}.scE5x5',
    objectGenMotherPdgId = '? (getDaughterGenParticleMotherSmart({object_idx}).isAvailable && getDaughterGenParticleMotherSmart({object_idx}).isNonnull) ? getDaughterGenParticleMotherSmart({object_idx}).pdgId() : -999',
    objectComesFromHiggs = 'comesFromHiggs({object_idx})',        
)

energyCorrections = PSet(
    objectECorrSmearedNoReg_2012Jul13ReReco = 'getUserLorentzVector({object_idx},"EGCorr_SmearedNoRegression_2012Jul13ReReco").t',
    objectdECorrSmearedNoReg_2012Jul13ReReco = '{object}.userFloat("EGCorr_SmearedNoRegression_2012Jul13ReReco_error")',
    objectECorrSmearedReg_2012Jul13ReReco = 'getUserLorentzVector({object_idx},"EGCorr_SmearedRegression_2012Jul13ReReco").t',
    objectdECorrSmearedReg_2012Jul13ReReco = '{object}.userFloat("EGCorr_SmearedRegression_2012Jul13ReReco_error")',
    objectECorrReg_2012Jul13ReReco = 'getUserLorentzVector({object_idx},"EGCorr_RegressionOnly_2012Jul13ReReco").t',
    objectdECorrReg_2012Jul13ReReco = '{object}.userFloat("EGCorr_RegressionOnly_2012Jul13ReReco_error")',

    objectECorrSmearedNoReg_Summer12_DR53X_HCP2012 = 'getUserLorentzVector({object_idx},"EGCorr_SmearedNoRegression_Summer12_DR53X_HCP2012").t',
    objectdECorrSmearedNoReg_Summer12_DR53X_HCP2012 = '{object}.userFloat("EGCorr_SmearedNoRegression_Summer12_DR53X_HCP2012_error")',
    objectECorrSmearedReg_Summer12_DR53X_HCP2012 = 'getUserLorentzVector({object_idx},"EGCorr_SmearedRegression_Summer12_DR53X_HCP2012").t',
    objectdECorrSmearedReg_Summer12_DR53X_HCP2012 = '{object}.userFloat("EGCorr_SmearedRegression_Summer12_DR53X_HCP2012_error")',
    objectECorrReg_Summer12_DR53X_HCP2012 = 'getUserLorentzVector({object_idx},"EGCorr_RegressionOnly_Summer12_DR53X_HCP2012").t',
    objectdECorrReg_Summer12_DR53X_HCP2012 = '{object}.userFloat("EGCorr_RegressionOnly_Summer12_DR53X_HCP2012_error")',

    objectECorrSmearedNoReg_Jan16ReReco = 'getUserLorentzVector({object_idx},"EGCorr_SmearedNoRegression_Jan16ReReco").t',
    objectdECorrSmearedNoReg_Jan16ReReco = '{object}.userFloat("EGCorr_SmearedNoRegression_Jan16ReReco_error")',
    objectECorrSmearedReg_Jan16ReReco = 'getUserLorentzVector({object_idx},"EGCorr_SmearedRegression_Jan16ReReco").t',
    objectdECorrSmearedReg_Jan16ReReco = '{object}.userFloat("EGCorr_SmearedRegression_Jan16ReReco_error")',
    objectECorrReg_Jan16ReReco = 'getUserLorentzVector({object_idx},"EGCorr_RegressionOnly_Jan16ReReco").t',
    objectdECorrReg_Jan16ReReco = '{object}.userFloat("EGCorr_RegressionOnly_Jan16ReReco_error")',

    objectECorrSmearedNoReg_Fall11 = 'getUserLorentzVector({object_idx},"EGCorr_SmearedNoRegression_Fall11").t',
    objectdECorrSmearedNoReg_Fall11 = '{object}.userFloat("EGCorr_SmearedNoRegression_Fall11_error")',
    objectECorrSmearedReg_Fall11 = 'getUserLorentzVector({object_idx},"EGCorr_SmearedRegression_Fall11").t',
    objectdECorrSmearedReg_Fall11 = '{object}.userFloat("EGCorr_SmearedRegression_Fall11_error")',
    objectECorrReg_Fall11 = 'getUserLorentzVector({object_idx},"EGCorr_RegressionOnly_Fall11").t',
    objectdECorrReg_Fall11 = '{object}.userFloat("EGCorr_RegressionOnly_Fall11_error")'
)

tracking = PSet(
    objectHasConversion = '{object}.userFloat("hasConversion")',
    objectMissingHits = cms.string(
        '? {object}.gsfTrack.isNonnull? '
        '{object}.gsfTrack.trackerExpectedHitsInner.numberOfHits() : 10'),
)

# Information about the matched supercluster
supercluster = PSet(
    objectSCEta = '{object}.superCluster().eta',
    objectSCPhi = '{object}.superCluster().phi',
    objectSCEnergy = '{object}.superCluster().energy',
    objectSCRawEnergy = '{object}.superCluster().rawEnergy',
    objectSCPreshowerEnergy = '{object}.superCluster().preshowerEnergy',
    objectSCPhiWidth = '{object}.superCluster().phiWidth',
    objectSCEtaWidth = '{object}.superCluster().etaWidth'   
)

trigger = PSet(
    objectMu17Ele8dZFilter  = 'matchToHLTFilter({object_idx}, "hltMu17Ele8dZFilter")', # HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v4-v6
    objectMu17Ele8CaloIdTPixelMatchFilter  = 'matchToHLTFilter({object_idx}, "hltMu17Ele8CaloIdTPixelMatchFilter")',
    objectL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter  = 'matchToHLTFilter({object_idx}, "hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter")',
    objectMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter  = 'matchToHLTFilter({object_idx}, "hltMu17Ele8CaloIdTCaloIsoVLTrkIdVLTrkIsoVLTrackIsoFilter")',
    objectEle27WP80TrackIsoMatchFilter = 'matchToHLTFilter({object_idx}, "hltEle27WP80TrackIsoFilter")',
    objectEle32WP70PFMT50PFMTFilter = 'matchToHLTFilter({object_idx},"hltEle32WP70PFMT50PFMTFilter")',
    objectEle27WP80PFMT50PFMTFilter = 'matchToHLTFilter({object_idx},"hltEle27WP80PFMT50PFMTFilter")',
    objectMatchesDoubleEPath       = r'matchToHLTPath({object_idx}, "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v\\d+,HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v\\d+")',
    objectMatchesMu17Ele8Path      = r'matchToHLTPath({object_idx}, "HLT_Mu17_Ele8_CaloIdL_v\\d+,HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_v\\d+,HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v\\d+")',
    objectMatchesMu8Ele17Path      = r'matchToHLTPath({object_idx}, "HLT_Mu8_Ele17_CaloIdL_v\\d+,HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_v\\d+")',
    objectMatchesSingleE    = r'matchToHLTPath({object_idx}, "HLT_Ele27_WP80_v\\d+,HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v\\d+,HLT_Ele32_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v\\d+")',
    objectMatchesSingleEPlusMET = r'matchToHLTPath({object_idx},"HLT_Ele27_WP80_PFMET_MT50_v\\d+,HLT_Ele32_WP70_PFMT50_v\\d+"',
)
