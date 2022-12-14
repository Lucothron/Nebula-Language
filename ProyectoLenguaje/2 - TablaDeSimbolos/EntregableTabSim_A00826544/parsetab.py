
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTDIVleftPOWERAND AS COLON COMMA COMMENT DIM DIV DO ELSE END ENDIF EQ EQUAL FLOAT FOR GE GOSUB GT ID IF IN INT LBRACK LE LET LOOP LPAREN LT MAT MINUS MULT NE NEXT NFLOAT NINT NOT OR PEND PLUS POWER PRINT PROGRAM RBRACK RPAREN SUBEND SUBPROCEDURE THEN VEC WEND WHILE\n    START : PROGRAM V P S PEND\n    \n    V : DIM ID AS VARTYPE V\n    \n    V : LET ID EQUAL VAR V S\n    \n    V : EMPTY\n    \n    P : SUBPROCEDURE LPAREN ID RPAREN V P S END\n    \n    P : IN LPAREN NUMTYPE RPAREN S\n    \n    P : PRINT LPAREN NUMTYPE RPAREN S\n    \n    P : EMPTY\n    \n    S : IF LPAREN RELEXPR RPAREN THEN S IFELSE END S\n    \n    IFELSE : ELSE THEN S\n    |\n    \n    S : WHILE LPAREN RELEXPR RPAREN S WEND S\n    \n    S : DO COLON S WHILE LPAREN RELEXPR RPAREN S\n    \n    S : FOR LPAREN RELEXPR RPAREN S END S\n    \n    S : O\n    \n    S : EMPTY\n    \n    VARTYPE : INT\n    | FLOAT\n    | VECDEF\n    | MATDEF\n    \n    NUMTYPE : ID\n    | NINT\n    | NFLOAT\n    \n    VAR : NINT\n    | NFLOAT\n    | VECTOR\n    | MATRIX\n    | ID\n    \n    VECDEF : VEC LBRACK RBRACK\n    \n    MATDEF : MAT LBRACK RBRACK\n    \n    VECTOR : LBRACK NUMTYPE RBRACK\n    \n    MATRIX : LBRACK NUMTYPE COMMA NUMTYPE RBRACK\n    \n    RELEXPR : VAR LT VAR\n    | VAR LE VAR\n    | VAR GT VAR\n    | VAR GE VAR\n    | VAR EQ VAR\n    | VAR NE VAR\n    \n    O : O EQUAL O\n    \n    O : O PLUS TIER1\n    | O MINUS TIER1\n    \n    TIER1 : TIER1 MULT TIER2\n    | TIER1 DIV TIER2\n    \n    TIER2 : LPAREN O RPAREN\n    \n    O : TIER1\n    \n    TIER1 : TIER2\n    \n    TIER2 : VAR\n    \n    EMPTY : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,36,],[0,-1,]),'DIM':([2,25,26,27,28,29,54,55,56,57,58,61,73,75,96,97,109,],[4,-24,-25,-26,-27,-28,4,-17,-18,-19,-20,4,-31,4,-29,-30,-32,]),'LET':([2,25,26,27,28,29,54,55,56,57,58,61,73,75,96,97,109,],[5,-24,-25,-26,-27,-28,5,-17,-18,-19,-20,5,-31,5,-29,-30,-32,]),'SUBPROCEDURE':([2,3,6,20,21,22,23,24,25,26,27,28,29,54,55,56,57,58,61,64,68,69,70,71,72,73,75,78,81,93,96,97,98,109,112,114,118,119,120,122,124,125,],[-48,8,-4,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,-2,-48,8,-29,-30,-3,-32,-48,-48,-12,-48,-14,-48,-13,-9,]),'IN':([2,3,6,20,21,22,23,24,25,26,27,28,29,54,55,56,57,58,61,64,68,69,70,71,72,73,75,78,81,93,96,97,98,109,112,114,118,119,120,122,124,125,],[-48,9,-4,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,-2,-48,9,-29,-30,-3,-32,-48,-48,-12,-48,-14,-48,-13,-9,]),'PRINT':([2,3,6,20,21,22,23,24,25,26,27,28,29,54,55,56,57,58,61,64,68,69,70,71,72,73,75,78,81,93,96,97,98,109,112,114,118,119,120,122,124,125,],[-48,10,-4,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,-2,-48,10,-29,-30,-3,-32,-48,-48,-12,-48,-14,-48,-13,-9,]),'IF':([2,3,6,7,11,20,21,22,23,24,25,26,27,28,29,40,54,55,56,57,58,61,64,68,69,70,71,72,73,75,76,77,78,81,89,91,93,94,95,96,97,98,99,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,15,-8,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,15,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,15,15,-2,15,15,15,-48,-6,-7,-29,-30,-3,15,-32,15,15,15,-12,15,-14,-5,15,15,-13,-9,]),'WHILE':([2,3,6,7,11,20,21,22,23,24,25,26,27,28,29,40,54,55,56,57,58,61,64,66,68,69,70,71,72,73,75,76,77,78,81,89,91,93,94,95,96,97,98,99,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,17,-8,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,17,-48,-17,-18,-19,-20,-48,-44,90,-39,-40,-41,-42,-43,-31,-48,17,17,-2,17,17,17,-48,-6,-7,-29,-30,-3,17,-32,17,17,17,-12,17,-14,-5,17,17,-13,-9,]),'DO':([2,3,6,7,11,20,21,22,23,24,25,26,27,28,29,40,54,55,56,57,58,61,64,68,69,70,71,72,73,75,76,77,78,81,89,91,93,94,95,96,97,98,99,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,18,-8,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,18,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,18,18,-2,18,18,18,-48,-6,-7,-29,-30,-3,18,-32,18,18,18,-12,18,-14,-5,18,18,-13,-9,]),'FOR':([2,3,6,7,11,20,21,22,23,24,25,26,27,28,29,40,54,55,56,57,58,61,64,68,69,70,71,72,73,75,76,77,78,81,89,91,93,94,95,96,97,98,99,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,19,-8,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,19,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,19,19,-2,19,19,19,-48,-6,-7,-29,-30,-3,19,-32,19,19,19,-12,19,-14,-5,19,19,-13,-9,]),'LPAREN':([2,3,6,7,8,9,10,11,15,16,17,19,20,21,22,23,24,25,26,27,28,29,40,42,43,44,45,46,54,55,56,57,58,61,64,68,69,70,71,72,73,75,76,77,78,81,89,90,91,93,94,95,96,97,98,99,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,16,31,32,33,-8,37,16,39,41,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,16,16,16,16,16,16,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,16,16,-2,16,16,107,16,-48,-6,-7,-29,-30,-3,16,-32,16,16,16,-12,16,-14,-5,16,16,-13,-9,]),'NINT':([2,3,6,7,11,16,20,21,22,23,24,25,26,27,28,29,30,32,33,35,37,39,40,41,42,43,44,45,46,54,55,56,57,58,61,64,68,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,91,93,94,95,96,97,98,99,107,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,25,-8,25,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,49,49,49,25,25,25,25,25,25,25,25,25,25,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,49,-48,25,25,-2,25,25,25,25,25,25,25,25,25,-48,-6,-7,-29,-30,-3,25,25,-32,25,25,25,-12,25,-14,-5,25,25,-13,-9,]),'NFLOAT':([2,3,6,7,11,16,20,21,22,23,24,25,26,27,28,29,30,32,33,35,37,39,40,41,42,43,44,45,46,54,55,56,57,58,61,64,68,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,91,93,94,95,96,97,98,99,107,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,26,-8,26,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,50,50,50,26,26,26,26,26,26,26,26,26,26,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,50,-48,26,26,-2,26,26,26,26,26,26,26,26,26,-48,-6,-7,-29,-30,-3,26,26,-32,26,26,26,-12,26,-14,-5,26,26,-13,-9,]),'ID':([2,3,4,5,6,7,11,16,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,39,40,41,42,43,44,45,46,54,55,56,57,58,61,64,68,69,70,71,72,73,74,75,76,77,78,81,83,84,85,86,87,88,89,91,93,94,95,96,97,98,99,107,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,12,13,-4,29,-8,29,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,48,51,48,48,29,29,29,29,29,29,29,29,29,29,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,48,-48,29,29,-2,29,29,29,29,29,29,29,29,29,-48,-6,-7,-29,-30,-3,29,29,-32,29,29,29,-12,29,-14,-5,29,29,-13,-9,]),'LBRACK':([2,3,6,7,11,16,20,21,22,23,24,25,26,27,28,29,35,37,39,40,41,42,43,44,45,46,54,55,56,57,58,59,60,61,64,68,69,70,71,72,73,75,76,77,78,81,83,84,85,86,87,88,89,91,93,94,95,96,97,98,99,107,109,110,112,114,118,119,120,121,122,123,124,125,],[-48,-48,-4,30,-8,30,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,30,30,30,30,30,30,30,30,30,30,-48,-17,-18,-19,-20,79,80,-48,-44,-39,-40,-41,-42,-43,-31,-48,30,30,-2,30,30,30,30,30,30,30,30,30,-48,-6,-7,-29,-30,-3,30,30,-32,30,30,30,-12,30,-14,-5,30,30,-13,-9,]),'PEND':([2,3,6,7,11,14,20,21,22,23,24,25,26,27,28,29,54,55,56,57,58,61,64,68,69,70,71,72,73,76,77,78,81,94,95,96,97,98,109,112,114,118,119,120,121,122,124,125,],[-48,-48,-4,-48,-8,36,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,-48,-2,-48,-6,-7,-29,-30,-3,-32,-48,-48,-12,-48,-14,-5,-48,-13,-9,]),'END':([6,11,20,21,22,23,24,25,26,27,28,29,54,55,56,57,58,61,64,68,69,70,71,72,73,75,76,77,78,81,91,93,94,95,96,97,98,99,108,109,110,111,112,114,115,116,118,119,120,121,122,123,124,125,126,],[-4,-8,-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-48,-17,-18,-19,-20,-48,-44,-39,-40,-41,-42,-43,-31,-48,-48,-48,-2,-48,-48,-48,-6,-7,-29,-30,-3,-48,114,-32,-48,-11,-48,-48,121,122,-12,-48,-14,-5,-48,-48,-13,-9,-10,]),'AS':([12,],[34,]),'EQUAL':([13,20,22,23,24,25,26,27,28,29,38,64,68,69,70,71,72,73,109,],[35,42,-45,-46,-47,-24,-25,-26,-27,-28,42,-44,42,-40,-41,-42,-43,-31,-32,]),'COLON':([18,],[40,]),'WEND':([20,21,22,23,24,25,26,27,28,29,64,68,69,70,71,72,73,89,106,109,112,114,118,119,120,122,124,125,],[-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-44,-39,-40,-41,-42,-43,-31,-48,112,-32,-48,-48,-12,-48,-14,-48,-13,-9,]),'ELSE':([20,21,22,23,24,25,26,27,28,29,64,68,69,70,71,72,73,99,109,111,112,114,118,119,120,122,124,125,],[-15,-16,-45,-46,-47,-24,-25,-26,-27,-28,-44,-39,-40,-41,-42,-43,-31,-48,-32,117,-48,-48,-12,-48,-14,-48,-13,-9,]),'PLUS':([20,22,23,24,25,26,27,28,29,38,64,68,69,70,71,72,73,109,],[43,-45,-46,-47,-24,-25,-26,-27,-28,43,-44,43,-40,-41,-42,-43,-31,-32,]),'MINUS':([20,22,23,24,25,26,27,28,29,38,64,68,69,70,71,72,73,109,],[44,-45,-46,-47,-24,-25,-26,-27,-28,44,-44,44,-40,-41,-42,-43,-31,-32,]),'RPAREN':([22,23,24,25,26,27,28,29,38,48,49,50,51,52,53,62,64,65,67,68,69,70,71,72,73,100,101,102,103,104,105,109,113,],[-45,-46,-47,-24,-25,-26,-27,-28,64,-21,-22,-23,75,76,77,82,-44,89,91,-39,-40,-41,-42,-43,-31,-33,-34,-35,-36,-37,-38,-32,119,]),'MULT':([22,23,24,25,26,27,28,29,64,69,70,71,72,73,109,],[45,-46,-47,-24,-25,-26,-27,-28,-44,45,45,-42,-43,-31,-32,]),'DIV':([22,23,24,25,26,27,28,29,64,69,70,71,72,73,109,],[46,-46,-47,-24,-25,-26,-27,-28,-44,46,46,-42,-43,-31,-32,]),'LT':([25,26,27,28,29,63,73,109,],[-24,-25,-26,-27,-28,83,-31,-32,]),'LE':([25,26,27,28,29,63,73,109,],[-24,-25,-26,-27,-28,84,-31,-32,]),'GT':([25,26,27,28,29,63,73,109,],[-24,-25,-26,-27,-28,85,-31,-32,]),'GE':([25,26,27,28,29,63,73,109,],[-24,-25,-26,-27,-28,86,-31,-32,]),'EQ':([25,26,27,28,29,63,73,109,],[-24,-25,-26,-27,-28,87,-31,-32,]),'NE':([25,26,27,28,29,63,73,109,],[-24,-25,-26,-27,-28,88,-31,-32,]),'INT':([34,],[55,]),'FLOAT':([34,],[56,]),'VEC':([34,],[59,]),'MAT':([34,],[60,]),'RBRACK':([47,48,49,50,79,80,92,],[73,-21,-22,-23,96,97,109,]),'COMMA':([47,48,49,50,],[74,-21,-22,-23,]),'THEN':([82,117,],[99,123,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[1,]),'V':([2,54,61,75,],[3,78,81,93,]),'EMPTY':([2,3,7,40,54,61,75,76,77,81,89,91,93,99,110,112,114,119,122,123,],[6,11,21,21,6,6,6,21,21,21,21,21,11,21,21,21,21,21,21,21,]),'P':([3,93,],[7,110,]),'S':([7,40,76,77,81,89,91,99,110,112,114,119,122,123,],[14,66,94,95,98,106,108,111,115,118,120,124,125,126,]),'O':([7,16,40,42,76,77,81,89,91,99,110,112,114,119,122,123,],[20,38,20,68,20,20,20,20,20,20,20,20,20,20,20,20,]),'TIER1':([7,16,40,42,43,44,76,77,81,89,91,99,110,112,114,119,122,123,],[22,22,22,22,69,70,22,22,22,22,22,22,22,22,22,22,22,22,]),'TIER2':([7,16,40,42,43,44,45,46,76,77,81,89,91,99,110,112,114,119,122,123,],[23,23,23,23,23,23,71,72,23,23,23,23,23,23,23,23,23,23,23,23,]),'VAR':([7,16,35,37,39,40,41,42,43,44,45,46,76,77,81,83,84,85,86,87,88,89,91,99,107,110,112,114,119,122,123,],[24,24,61,63,63,24,63,24,24,24,24,24,24,24,24,100,101,102,103,104,105,24,24,24,63,24,24,24,24,24,24,]),'VECTOR':([7,16,35,37,39,40,41,42,43,44,45,46,76,77,81,83,84,85,86,87,88,89,91,99,107,110,112,114,119,122,123,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'MATRIX':([7,16,35,37,39,40,41,42,43,44,45,46,76,77,81,83,84,85,86,87,88,89,91,99,107,110,112,114,119,122,123,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'NUMTYPE':([30,32,33,74,],[47,52,53,92,]),'VARTYPE':([34,],[54,]),'VECDEF':([34,],[57,]),'MATDEF':([34,],[58,]),'RELEXPR':([37,39,41,107,],[62,65,67,113,]),'IFELSE':([111,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> PROGRAM V P S PEND','START',5,'p_START','nebulaSyn.py',24),
  ('V -> DIM ID AS VARTYPE V','V',5,'p_V_DIM','nebulaSyn.py',33),
  ('V -> LET ID EQUAL VAR V S','V',6,'p_V_LET','nebulaSyn.py',43),
  ('V -> EMPTY','V',1,'p_V_EMPTY','nebulaSyn.py',48),
  ('P -> SUBPROCEDURE LPAREN ID RPAREN V P S END','P',8,'p_P_SUB','nebulaSyn.py',55),
  ('P -> IN LPAREN NUMTYPE RPAREN S','P',5,'p_P_INP','nebulaSyn.py',60),
  ('P -> PRINT LPAREN NUMTYPE RPAREN S','P',5,'p_P_PRINT','nebulaSyn.py',65),
  ('P -> EMPTY','P',1,'p_P_EMPTY','nebulaSyn.py',70),
  ('S -> IF LPAREN RELEXPR RPAREN THEN S IFELSE END S','S',9,'p_S_IF','nebulaSyn.py',77),
  ('IFELSE -> ELSE THEN S','IFELSE',3,'p_S_IFELSE','nebulaSyn.py',82),
  ('IFELSE -> <empty>','IFELSE',0,'p_S_IFELSE','nebulaSyn.py',83),
  ('S -> WHILE LPAREN RELEXPR RPAREN S WEND S','S',7,'p_S_WHILE','nebulaSyn.py',88),
  ('S -> DO COLON S WHILE LPAREN RELEXPR RPAREN S','S',8,'p_S_DO','nebulaSyn.py',93),
  ('S -> FOR LPAREN RELEXPR RPAREN S END S','S',7,'p_S_FOR','nebulaSyn.py',98),
  ('S -> O','S',1,'p_S_OPERATION','nebulaSyn.py',103),
  ('S -> EMPTY','S',1,'p_S_EMPTY','nebulaSyn.py',108),
  ('VARTYPE -> INT','VARTYPE',1,'p_VARTYPE','nebulaSyn.py',115),
  ('VARTYPE -> FLOAT','VARTYPE',1,'p_VARTYPE','nebulaSyn.py',116),
  ('VARTYPE -> VECDEF','VARTYPE',1,'p_VARTYPE','nebulaSyn.py',117),
  ('VARTYPE -> MATDEF','VARTYPE',1,'p_VARTYPE','nebulaSyn.py',118),
  ('NUMTYPE -> ID','NUMTYPE',1,'p_NUMTYPE','nebulaSyn.py',124),
  ('NUMTYPE -> NINT','NUMTYPE',1,'p_NUMTYPE','nebulaSyn.py',125),
  ('NUMTYPE -> NFLOAT','NUMTYPE',1,'p_NUMTYPE','nebulaSyn.py',126),
  ('VAR -> NINT','VAR',1,'p_VAR','nebulaSyn.py',131),
  ('VAR -> NFLOAT','VAR',1,'p_VAR','nebulaSyn.py',132),
  ('VAR -> VECTOR','VAR',1,'p_VAR','nebulaSyn.py',133),
  ('VAR -> MATRIX','VAR',1,'p_VAR','nebulaSyn.py',134),
  ('VAR -> ID','VAR',1,'p_VAR','nebulaSyn.py',135),
  ('VECDEF -> VEC LBRACK RBRACK','VECDEF',3,'p_VECDEF','nebulaSyn.py',140),
  ('MATDEF -> MAT LBRACK RBRACK','MATDEF',3,'p_MATDEF','nebulaSyn.py',146),
  ('VECTOR -> LBRACK NUMTYPE RBRACK','VECTOR',3,'p_VECTOR','nebulaSyn.py',152),
  ('MATRIX -> LBRACK NUMTYPE COMMA NUMTYPE RBRACK','MATRIX',5,'p_MATRIX','nebulaSyn.py',157),
  ('RELEXPR -> VAR LT VAR','RELEXPR',3,'p_RELEXPR','nebulaSyn.py',162),
  ('RELEXPR -> VAR LE VAR','RELEXPR',3,'p_RELEXPR','nebulaSyn.py',163),
  ('RELEXPR -> VAR GT VAR','RELEXPR',3,'p_RELEXPR','nebulaSyn.py',164),
  ('RELEXPR -> VAR GE VAR','RELEXPR',3,'p_RELEXPR','nebulaSyn.py',165),
  ('RELEXPR -> VAR EQ VAR','RELEXPR',3,'p_RELEXPR','nebulaSyn.py',166),
  ('RELEXPR -> VAR NE VAR','RELEXPR',3,'p_RELEXPR','nebulaSyn.py',167),
  ('O -> O EQUAL O','O',3,'p_O_EQUAL','nebulaSyn.py',172),
  ('O -> O PLUS TIER1','O',3,'p_O_MATHTIER1','nebulaSyn.py',177),
  ('O -> O MINUS TIER1','O',3,'p_O_MATHTIER1','nebulaSyn.py',178),
  ('TIER1 -> TIER1 MULT TIER2','TIER1',3,'p_O_MATHTIER2','nebulaSyn.py',183),
  ('TIER1 -> TIER1 DIV TIER2','TIER1',3,'p_O_MATHTIER2','nebulaSyn.py',184),
  ('TIER2 -> LPAREN O RPAREN','TIER2',3,'p_O_MATHTIER3','nebulaSyn.py',189),
  ('O -> TIER1','O',1,'p_O_T1','nebulaSyn.py',194),
  ('TIER1 -> TIER2','TIER1',1,'p_O_T2','nebulaSyn.py',199),
  ('TIER2 -> VAR','TIER2',1,'p_O_T3','nebulaSyn.py',204),
  ('EMPTY -> <empty>','EMPTY',0,'p_EMPTY','nebulaSyn.py',209),
]
