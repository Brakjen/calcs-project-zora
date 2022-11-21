MW='/cluster/home/ambr/projects/zora/small_molecules/calcs'
GTO='/home/ambr/projects/zora/small_molecules_gto/calcs'
MW_NREL='/cluster/home/ambr/projects/zora/small_molecules/calcs_nrel'
GTO_NREL_UGBS='/home/ambr/projects/zora/small_molecules_gto/calcs_nrel_ugbs'
GTO_NREL_SARC='/home/ambr/projects/zora/small_molecules_gto/calcs_nrel_sarczorabasis'

echo MW ZORA
scp betzy:${MW}/* calcs_mw

echo MW NREL
scp betzy:${MW_NREL}/* calcs_mw_nrel

echo GTO ZORA
scp woolf:${GTO}/* calcs_gto

echo GTO NREL UGBS
scp woolf:${GTO_NREL_UGBS}/* calcs_gto_nrel_ugbs

echo GTO NREL SARC
scp woolf:${GTO_NREL_SARC}/* calcs_gto_nrel_sarczorabasis
