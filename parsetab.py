
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERS AND ARRAY ARROW AT BEGIN BOOLAND BOOLOR BREAK CASE CLASS COLON COMMA COMMENT COMPX DEF DIVIDE DO DOLLARSGN DOT DUODOT ELSE ELSIF END ENSURE EQCOMP EQUALS EXPON FALSE FLOAT FOR GREATEQTH GREATH HASH ID IF IN INT LBRACE LBRAKET LESSEQTH LESSTH LPAREN MATRIX MINUS MINUSEQ MODULE NEW NEXT NIL NOT NOTEQ OR PIPE PLUS PLUSEQ RAT RBRACE RBRAKET RETRY RETURN ROCKET RPAREN SELF SEMICOLON SET STRING SUPER THEN TILDE TIMES TRIDOT TRUE UNDERSCR UNLESS UNTIL WHEN WHILEinit : cmmdbool : TRUE\n    | FALSE\n    num : INT\n    | FLOAT\n    | RAT\n    | COMPX\n    optn : num PLUS numoptn : num MINUS numoptn : num TIMES numoptn : num DIVIDE numoptn : num MODULE numoptn : num EXPON numoptns : optn PLUS numoptns : optn MINUS numoptns : optn TIMES numoptns : optn DIVIDE numoptns : optn MODULE numoptns : optn EXPON numcomptr : EQCOMP\n    | LESSTH\n    | LESSEQTH\n    | GREATH\n    | GREATEQTH\n    | NOTEQ\n    comptn : obj comptr obj\n    | ID comptr ID\n    comptns : comptn\n    | comptn comptr obj\n    | comptn comptr ID\n    | comptn comptr comptns\n    and : AND\n    | BOOLAND\n    or : OR\n    | BOOLOR\n    var : ID EQUALS obj\n    | ID EQUALS struc\n    | ID EQUALS ID\n    | ID EQUALS NIL\n    | ID EQUALS optns\n    func : DEF ID LPAREN objs RPAREN cmmd END\n    | DEF ID LPAREN RPAREN cmmd END\n    | DEF ID cmmd END\n    | DEF ID LPAREN objs RPAREN cmmd RETURN obj END\n    | DEF ID LPAREN RPAREN cmmd RETURN obj END\n    | DEF ID cmmd RETURN obj END\n    else : ELSE comptn cmmd\n    | ELSE bool cmmd\n    elsif : ELSIF comptn cmmd\n    | ELSIF bool cmmd\n    elses : else\n    | elsif elses\n    control : IF comptn cmmd END\n    | IF bool cmmd END\n    | IF comptn cmmd elses END\n    | IF bool cmmd elses END\n    control : UNLESS comptn COLON cmmd END\n    | UNLESS bool COLON cmmd END\n    | UNLESS comptn cmmd elses END\n    | UNLESS bool cmmd elses END\n    control : CASE ID whens else END\n    | CASE ID whens END\n    control : WHILE comptn DO cmmd END\n    | WHILE bool DO cmmd END\n    when : WHEN objs\n    | WHEN objs THEN\n    | WHEN comptn\n    whens : when\n    | when whens\n    ids : ID\n    | ID COMMA ids\n    array : LBRAKET objs RBRAKET\n    | LBRAKET ids RBRAKET\n    | LBRAKET objs COMMA ids RBRAKET\n    | LBRAKET ids COMMA objs RBRAKET\n    arrays : array\n    | array COMMA arrays\n    strucMatrix : MATRIX LBRAKET arrays RBRAKETstrucSet : SET DOT NEW\n    | SET DOT NEW LPAREN RPAREN\n    | SET DOT NEW LPAREN array RPAREN\n    | SET array\n    strucHash : HASH DOT NEW\n    | HASH DOT NEW LBRACE RBRACE\n    | HASH DOT NEW LBRACE hashelems RBRACE\n    | HASH array\n    hashelem : COLON ID ROCKET objhashelem : ID COLON objhashelem : STRING COLON objhashelems : hashelem COMMA hashelem\n    | hashelem COMMA hashelems\n    objs : obj\n    | obj COMMA objs\n    obj : STRING\n    | num\n    | bool\n    | range\n    struc : strucMatrix\n    | strucSet\n    | strucHash\n    range : LPAREN INT DOT DOT INT RPAREN\n    | INT DOT DOT INT\n    | LPAREN STRING DOT DOT STRING\n    | STRING DOT DOT STRING\n    cmmd : var\n    | func\n    | control\n    | optns\n    '
    
_lr_action_items = {'ID':([0,8,9,10,11,12,16,17,18,19,20,21,22,25,26,27,28,29,30,32,33,55,67,68,69,70,71,72,73,78,80,84,85,86,102,106,114,115,118,119,143,149,150,151,152,154,155,170,173,174,185,195,201,206,],[7,20,24,24,34,24,-5,-6,-7,49,7,7,7,-2,-3,-94,-95,-97,-4,7,7,-96,-20,-21,-22,-23,-24,-25,119,7,7,24,7,7,141,7,24,24,-26,-27,7,7,7,7,7,-104,-102,141,141,196,-103,207,-101,196,]),'DEF':([0,16,17,18,20,21,22,25,26,27,28,29,30,32,33,55,78,80,85,86,106,118,119,143,149,150,151,152,154,155,185,201,],[8,-5,-6,-7,8,8,8,-2,-3,-94,-95,-97,-4,8,8,-96,8,8,8,8,8,-26,-27,8,8,8,8,8,-104,-102,-103,-101,]),'IF':([0,16,17,18,20,21,22,25,26,27,28,29,30,32,33,55,78,80,85,86,106,118,119,143,149,150,151,152,154,155,185,201,],[9,-5,-6,-7,9,9,9,-2,-3,-94,-95,-97,-4,9,9,-96,9,9,9,9,9,-26,-27,9,9,9,9,9,-104,-102,-103,-101,]),'UNLESS':([0,16,17,18,20,21,22,25,26,27,28,29,30,32,33,55,78,80,85,86,106,118,119,143,149,150,151,152,154,155,185,201,],[10,-5,-6,-7,10,10,10,-2,-3,-94,-95,-97,-4,10,10,-96,10,10,10,10,10,-26,-27,10,10,10,10,10,-104,-102,-103,-101,]),'CASE':([0,16,17,18,20,21,22,25,26,27,28,29,30,32,33,55,78,80,85,86,106,118,119,143,149,150,151,152,154,155,185,201,],[11,-5,-6,-7,11,11,11,-2,-3,-94,-95,-97,-4,11,11,-96,11,11,11,11,11,-26,-27,11,11,11,11,11,-104,-102,-103,-101,]),'WHILE':([0,16,17,18,20,21,22,25,26,27,28,29,30,32,33,55,78,80,85,86,106,118,119,143,149,150,151,152,154,155,185,201,],[12,-5,-6,-7,12,12,12,-2,-3,-94,-95,-97,-4,12,12,-96,12,12,12,12,12,-26,-27,12,12,12,12,12,-104,-102,-103,-101,]),'INT':([0,9,10,12,16,17,18,19,20,21,22,25,26,27,28,29,30,31,32,33,37,38,39,40,41,42,43,44,45,46,47,48,55,62,66,67,68,69,70,71,72,78,80,84,85,86,102,106,109,114,115,118,119,121,143,145,149,150,151,152,154,155,156,172,177,185,199,201,208,209,214,],[15,30,30,30,-5,-6,-7,30,15,15,15,-2,-3,-94,-95,-97,-4,76,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-96,30,30,-20,-21,-22,-23,-24,-25,15,15,30,15,15,30,15,30,30,30,-26,-27,155,15,30,15,15,15,15,-104,-102,184,30,30,-103,30,-101,30,30,30,]),'FLOAT':([0,9,10,12,16,17,18,19,20,21,22,25,26,27,28,29,30,32,33,37,38,39,40,41,42,43,44,45,46,47,48,55,62,66,67,68,69,70,71,72,78,80,84,85,86,102,106,109,114,115,118,119,143,145,149,150,151,152,154,155,172,177,185,199,201,208,209,214,],[16,16,16,16,-5,-6,-7,16,16,16,16,-2,-3,-94,-95,-97,-4,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-96,16,16,-20,-21,-22,-23,-24,-25,16,16,16,16,16,16,16,16,16,16,-26,-27,16,16,16,16,16,16,-104,-102,16,16,-103,16,-101,16,16,16,]),'RAT':([0,9,10,12,16,17,18,19,20,21,22,25,26,27,28,29,30,32,33,37,38,39,40,41,42,43,44,45,46,47,48,55,62,66,67,68,69,70,71,72,78,80,84,85,86,102,106,109,114,115,118,119,143,145,149,150,151,152,154,155,172,177,185,199,201,208,209,214,],[17,17,17,17,-5,-6,-7,17,17,17,17,-2,-3,-94,-95,-97,-4,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-96,17,17,-20,-21,-22,-23,-24,-25,17,17,17,17,17,17,17,17,17,17,-26,-27,17,17,17,17,17,17,-104,-102,17,17,-103,17,-101,17,17,17,]),'COMPX':([0,9,10,12,16,17,18,19,20,21,22,25,26,27,28,29,30,32,33,37,38,39,40,41,42,43,44,45,46,47,48,55,62,66,67,68,69,70,71,72,78,80,84,85,86,102,106,109,114,115,118,119,143,145,149,150,151,152,154,155,172,177,185,199,201,208,209,214,],[18,18,18,18,-5,-6,-7,18,18,18,18,-2,-3,-94,-95,-97,-4,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-96,18,18,-20,-21,-22,-23,-24,-25,18,18,18,18,18,18,18,18,18,18,-26,-27,18,18,18,18,18,18,-104,-102,18,18,-103,18,-101,18,18,18,]),'$end':([1,2,3,4,5,6,15,16,17,18,25,26,27,29,30,49,50,51,52,53,54,55,56,57,58,87,88,89,90,91,92,101,104,108,110,116,129,138,142,147,153,154,155,158,159,160,161,162,164,165,166,169,171,176,179,185,187,192,198,201,202,203,204,205,211,217,],[0,-1,-105,-106,-107,-108,-4,-5,-6,-7,-2,-3,-94,-97,-4,-38,-36,-37,-39,-40,-95,-96,-98,-99,-100,-14,-15,-16,-17,-18,-19,-82,-86,-43,-53,-54,-62,-79,-83,-55,-56,-104,-102,-57,-59,-58,-60,-61,-63,-64,-78,-72,-73,-42,-46,-103,-80,-84,-41,-101,-81,-74,-75,-85,-45,-44,]),'END':([3,4,5,6,15,16,17,18,25,26,27,28,29,30,49,50,51,52,53,54,55,56,57,58,63,64,65,82,83,87,88,89,90,91,92,101,104,107,108,110,111,112,116,117,118,119,124,125,126,127,128,129,130,131,132,133,134,135,138,142,144,146,147,148,153,154,155,158,159,160,161,162,163,164,165,166,169,171,175,176,178,179,180,181,185,187,192,198,200,201,202,203,204,205,210,211,217,],[-105,-106,-107,-108,-4,-5,-6,-7,-2,-3,-94,-95,-97,-4,-38,-36,-37,-39,-40,-95,-96,-98,-99,-100,108,110,116,129,-68,-14,-15,-16,-17,-18,-19,-82,-86,-92,-43,-53,147,-51,-54,153,-26,-27,158,159,160,161,162,-62,-69,-65,-67,-92,164,165,-79,-83,176,179,-55,-52,-56,-104,-102,-57,-59,-58,-60,-61,-66,-63,-64,-78,-72,-73,198,-42,-93,-46,-47,-48,-103,-80,-84,-41,211,-101,-81,-74,-75,-85,217,-45,-44,]),'RETURN':([3,4,5,6,15,16,17,18,25,26,27,29,30,49,50,51,52,53,54,55,56,57,58,63,87,88,89,90,91,92,101,104,108,110,116,129,138,142,144,147,153,154,155,158,159,160,161,162,164,165,166,169,171,175,176,179,185,187,192,198,201,202,203,204,205,211,217,],[-105,-106,-107,-108,-4,-5,-6,-7,-2,-3,-94,-97,-4,-38,-36,-37,-39,-40,-95,-96,-98,-99,-100,109,-14,-15,-16,-17,-18,-19,-82,-86,-43,-53,-54,-62,-79,-83,177,-55,-56,-104,-102,-57,-59,-58,-60,-61,-63,-64,-78,-72,-73,199,-42,-46,-103,-80,-84,-41,-101,-81,-74,-75,-85,-45,-44,]),'ELSE':([3,4,5,6,15,16,17,18,25,26,27,28,29,30,49,50,51,52,53,54,55,56,57,58,64,65,79,81,82,83,87,88,89,90,91,92,101,104,107,108,110,113,116,118,119,129,130,131,132,133,138,142,147,153,154,155,158,159,160,161,162,163,164,165,166,169,171,176,178,179,182,183,185,187,192,198,201,202,203,204,205,211,217,],[-105,-106,-107,-108,-4,-5,-6,-7,-2,-3,-94,-95,-97,-4,-38,-36,-37,-39,-40,-95,-96,-98,-99,-100,114,114,114,114,114,-68,-14,-15,-16,-17,-18,-19,-82,-86,-92,-43,-53,114,-54,-26,-27,-62,-69,-65,-67,-92,-79,-83,-55,-56,-104,-102,-57,-59,-58,-60,-61,-66,-63,-64,-78,-72,-73,-42,-93,-46,-49,-50,-103,-80,-84,-41,-101,-81,-74,-75,-85,-45,-44,]),'ELSIF':([3,4,5,6,15,16,17,18,25,26,27,29,30,49,50,51,52,53,54,55,56,57,58,64,65,79,81,87,88,89,90,91,92,101,104,108,110,113,116,129,138,142,147,153,154,155,158,159,160,161,162,164,165,166,169,171,176,179,182,183,185,187,192,198,201,202,203,204,205,211,217,],[-105,-106,-107,-108,-4,-5,-6,-7,-2,-3,-94,-97,-4,-38,-36,-37,-39,-40,-95,-96,-98,-99,-100,115,115,115,115,-14,-15,-16,-17,-18,-19,-82,-86,-43,-53,115,-54,-62,-79,-83,-55,-56,-104,-102,-57,-59,-58,-60,-61,-63,-64,-78,-72,-73,-42,-46,-49,-50,-103,-80,-84,-41,-101,-81,-74,-75,-85,-45,-44,]),'EQUALS':([7,],[19,]),'TRUE':([9,10,12,19,62,66,67,68,69,70,71,72,84,102,109,114,115,145,172,177,199,208,209,214,],[25,25,25,25,25,25,-20,-21,-22,-23,-24,-25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FALSE':([9,10,12,19,62,66,67,68,69,70,71,72,84,102,109,114,115,145,172,177,199,208,209,214,],[26,26,26,26,26,26,-20,-21,-22,-23,-24,-25,26,26,26,26,26,26,26,26,26,26,26,26,]),'STRING':([9,10,12,19,31,62,66,67,68,69,70,71,72,84,102,109,114,115,120,145,157,172,174,177,199,206,208,209,214,],[27,27,27,27,77,27,27,-20,-21,-22,-23,-24,-25,27,27,27,27,27,154,27,185,27,197,27,27,197,27,27,27,]),'LPAREN':([9,10,12,19,20,62,66,67,68,69,70,71,72,84,102,109,114,115,138,145,172,177,199,208,209,214,],[31,31,31,31,62,31,31,-20,-21,-22,-23,-24,-25,31,31,31,31,31,168,31,31,31,31,31,31,31,]),'PLUS':([13,14,15,16,17,18,30,54,93,94,95,96,97,98,],[37,43,-4,-5,-6,-7,-4,43,-8,-9,-10,-11,-12,-13,]),'MINUS':([13,14,15,16,17,18,30,54,93,94,95,96,97,98,],[38,44,-4,-5,-6,-7,-4,44,-8,-9,-10,-11,-12,-13,]),'TIMES':([13,14,15,16,17,18,30,54,93,94,95,96,97,98,],[39,45,-4,-5,-6,-7,-4,45,-8,-9,-10,-11,-12,-13,]),'DIVIDE':([13,14,15,16,17,18,30,54,93,94,95,96,97,98,],[40,46,-4,-5,-6,-7,-4,46,-8,-9,-10,-11,-12,-13,]),'MODULE':([13,14,15,16,17,18,30,54,93,94,95,96,97,98,],[41,47,-4,-5,-6,-7,-4,47,-8,-9,-10,-11,-12,-13,]),'EXPON':([13,14,15,16,17,18,30,54,93,94,95,96,97,98,],[42,48,-4,-5,-6,-7,-4,48,-8,-9,-10,-11,-12,-13,]),'EQCOMP':([16,17,18,22,23,24,25,26,27,28,29,30,33,36,55,133,150,152,154,155,185,201,],[-5,-6,-7,-96,67,67,-2,-3,-94,-95,-97,-4,-96,-96,-96,67,-96,-96,-104,-102,-103,-101,]),'LESSTH':([16,17,18,22,23,24,25,26,27,28,29,30,33,36,55,133,150,152,154,155,185,201,],[-5,-6,-7,-96,68,68,-2,-3,-94,-95,-97,-4,-96,-96,-96,68,-96,-96,-104,-102,-103,-101,]),'LESSEQTH':([16,17,18,22,23,24,25,26,27,28,29,30,33,36,55,133,150,152,154,155,185,201,],[-5,-6,-7,-96,69,69,-2,-3,-94,-95,-97,-4,-96,-96,-96,69,-96,-96,-104,-102,-103,-101,]),'GREATH':([16,17,18,22,23,24,25,26,27,28,29,30,33,36,55,133,150,152,154,155,185,201,],[-5,-6,-7,-96,70,70,-2,-3,-94,-95,-97,-4,-96,-96,-96,70,-96,-96,-104,-102,-103,-101,]),'GREATEQTH':([16,17,18,22,23,24,25,26,27,28,29,30,33,36,55,133,150,152,154,155,185,201,],[-5,-6,-7,-96,71,71,-2,-3,-94,-95,-97,-4,-96,-96,-96,71,-96,-96,-104,-102,-103,-101,]),'NOTEQ':([16,17,18,22,23,24,25,26,27,28,29,30,33,36,55,133,150,152,154,155,185,201,],[-5,-6,-7,-96,72,72,-2,-3,-94,-95,-97,-4,-96,-96,-96,72,-96,-96,-104,-102,-103,-101,]),'COMMA':([16,17,18,25,26,27,28,29,30,55,107,133,137,139,140,141,154,155,169,171,178,185,191,194,201,203,204,212,215,216,218,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,-96,145,145,167,170,172,173,-104,-102,-72,-73,-93,-103,-71,206,-101,-74,-75,206,-88,-89,-87,]),'RPAREN':([16,17,18,25,26,27,28,29,30,55,62,105,107,154,155,168,169,171,178,184,185,188,201,203,204,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,-96,106,143,-92,-104,-102,187,-72,-73,-93,201,-103,202,-101,-74,-75,]),'COLON':([16,17,18,25,26,27,28,29,30,32,33,55,118,119,154,155,174,185,196,197,201,206,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,78,80,-96,-26,-27,-104,-102,195,-103,208,209,-101,195,]),'DO':([16,17,18,25,26,27,28,29,30,35,36,55,118,119,154,155,185,201,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,85,86,-96,-26,-27,-104,-102,-103,-101,]),'WHEN':([16,17,18,25,26,27,28,29,30,34,55,83,107,118,119,131,132,133,154,155,163,178,185,201,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,84,-96,84,-92,-26,-27,-65,-67,-92,-104,-102,-66,-93,-103,-101,]),'THEN':([16,17,18,25,26,27,28,29,30,55,107,131,133,154,155,178,185,201,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,-96,-92,163,-92,-104,-102,-93,-103,-101,]),'RBRAKET':([16,17,18,25,26,27,28,29,30,55,107,136,137,139,140,141,154,155,169,171,178,185,186,189,190,191,201,203,204,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,-96,-92,166,-76,169,171,-70,-104,-102,-72,-73,-93,-103,-77,203,204,-71,-101,-74,-75,]),'RBRACE':([16,17,18,25,26,27,28,29,30,55,154,155,174,185,193,201,212,213,215,216,218,],[-5,-6,-7,-2,-3,-94,-95,-97,-4,-96,-104,-102,192,-103,205,-101,-90,-91,-88,-89,-87,]),'NIL':([19,],[52,]),'MATRIX':([19,],[59,]),'SET':([19,],[60,]),'HASH':([19,],[61,]),'DOT':([27,30,60,61,74,75,76,77,122,123,],[74,75,100,103,120,121,122,123,156,157,]),'LBRAKET':([59,60,61,99,167,168,],[99,102,102,102,102,102,]),'NEW':([100,103,],[138,142,]),'LBRACE':([142,],[174,]),'ROCKET':([207,],[214,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'cmmd':([0,20,21,22,32,33,78,80,85,86,106,143,149,150,151,152,],[2,63,64,65,79,81,124,126,134,135,144,175,180,181,182,183,]),'var':([0,20,21,22,32,33,78,80,85,86,106,143,149,150,151,152,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'func':([0,20,21,22,32,33,78,80,85,86,106,143,149,150,151,152,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'control':([0,20,21,22,32,33,78,80,85,86,106,143,149,150,151,152,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'optns':([0,19,20,21,22,32,33,78,80,85,86,106,143,149,150,151,152,],[6,53,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'optn':([0,19,20,21,22,32,33,78,80,85,86,106,143,149,150,151,152,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'num':([0,9,10,12,19,20,21,22,32,33,37,38,39,40,41,42,43,44,45,46,47,48,62,66,78,80,84,85,86,102,106,109,114,115,143,145,149,150,151,152,172,177,199,208,209,214,],[14,28,28,28,54,14,14,14,14,14,87,88,89,90,91,92,93,94,95,96,97,98,28,28,14,14,28,14,14,28,14,28,28,28,14,28,14,14,14,14,28,28,28,28,28,28,]),'comptn':([9,10,12,84,114,115,],[21,32,35,132,149,151,]),'bool':([9,10,12,19,62,66,84,102,109,114,115,145,172,177,199,208,209,214,],[22,33,36,55,55,55,55,55,55,150,152,55,55,55,55,55,55,55,]),'obj':([9,10,12,19,62,66,84,102,109,114,115,145,172,177,199,208,209,214,],[23,23,23,50,107,118,133,107,146,23,23,107,107,200,210,215,216,218,]),'range':([9,10,12,19,62,66,84,102,109,114,115,145,172,177,199,208,209,214,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'struc':([19,],[51,]),'strucMatrix':([19,],[56,]),'strucSet':([19,],[57,]),'strucHash':([19,],[58,]),'comptr':([23,24,133,],[66,73,66,]),'whens':([34,83,],[82,130,]),'when':([34,83,],[83,83,]),'array':([60,61,99,167,168,],[101,104,137,137,188,]),'objs':([62,84,102,145,172,],[105,131,139,178,190,]),'elses':([64,65,79,81,113,],[111,117,125,127,148,]),'else':([64,65,79,81,82,113,],[112,112,112,112,128,112,]),'elsif':([64,65,79,81,113,],[113,113,113,113,113,]),'arrays':([99,167,],[136,186,]),'ids':([102,170,173,],[140,189,191,]),'hashelems':([174,206,],[193,213,]),'hashelem':([174,206,],[194,212,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> cmmd','init',1,'p_init','semtic.py',17),
  ('bool -> TRUE','bool',1,'p_bool','semtic.py',21),
  ('bool -> FALSE','bool',1,'p_bool','semtic.py',22),
  ('num -> INT','num',1,'p_num','semtic.py',27),
  ('num -> FLOAT','num',1,'p_num','semtic.py',28),
  ('num -> RAT','num',1,'p_num','semtic.py',29),
  ('num -> COMPX','num',1,'p_num','semtic.py',30),
  ('optn -> num PLUS num','optn',3,'p_optn_plus','semtic.py',35),
  ('optn -> num MINUS num','optn',3,'p_optn_minus','semtic.py',40),
  ('optn -> num TIMES num','optn',3,'p_optn_times','semtic.py',45),
  ('optn -> num DIVIDE num','optn',3,'p_optn_divide','semtic.py',50),
  ('optn -> num MODULE num','optn',3,'p_optn_module','semtic.py',55),
  ('optn -> num EXPON num','optn',3,'p_optn_expon','semtic.py',60),
  ('optns -> optn PLUS num','optns',3,'p_optns_plus','semtic.py',65),
  ('optns -> optn MINUS num','optns',3,'p_optns_minus','semtic.py',70),
  ('optns -> optn TIMES num','optns',3,'p_optns_times','semtic.py',75),
  ('optns -> optn DIVIDE num','optns',3,'p_optns_divide','semtic.py',80),
  ('optns -> optn MODULE num','optns',3,'p_optns_module','semtic.py',85),
  ('optns -> optn EXPON num','optns',3,'p_optns_expon','semtic.py',90),
  ('comptr -> EQCOMP','comptr',1,'p_comptr','semtic.py',95),
  ('comptr -> LESSTH','comptr',1,'p_comptr','semtic.py',96),
  ('comptr -> LESSEQTH','comptr',1,'p_comptr','semtic.py',97),
  ('comptr -> GREATH','comptr',1,'p_comptr','semtic.py',98),
  ('comptr -> GREATEQTH','comptr',1,'p_comptr','semtic.py',99),
  ('comptr -> NOTEQ','comptr',1,'p_comptr','semtic.py',100),
  ('comptn -> obj comptr obj','comptn',3,'p_comptn','semtic.py',105),
  ('comptn -> ID comptr ID','comptn',3,'p_comptn','semtic.py',106),
  ('comptns -> comptn','comptns',1,'p_comptns','semtic.py',111),
  ('comptns -> comptn comptr obj','comptns',3,'p_comptns','semtic.py',112),
  ('comptns -> comptn comptr ID','comptns',3,'p_comptns','semtic.py',113),
  ('comptns -> comptn comptr comptns','comptns',3,'p_comptns','semtic.py',114),
  ('and -> AND','and',1,'p_and','semtic.py',119),
  ('and -> BOOLAND','and',1,'p_and','semtic.py',120),
  ('or -> OR','or',1,'p_or','semtic.py',125),
  ('or -> BOOLOR','or',1,'p_or','semtic.py',126),
  ('var -> ID EQUALS obj','var',3,'p_var','semtic.py',131),
  ('var -> ID EQUALS struc','var',3,'p_var','semtic.py',132),
  ('var -> ID EQUALS ID','var',3,'p_var','semtic.py',133),
  ('var -> ID EQUALS NIL','var',3,'p_var','semtic.py',134),
  ('var -> ID EQUALS optns','var',3,'p_var','semtic.py',135),
  ('func -> DEF ID LPAREN objs RPAREN cmmd END','func',7,'p_func','semtic.py',140),
  ('func -> DEF ID LPAREN RPAREN cmmd END','func',6,'p_func','semtic.py',141),
  ('func -> DEF ID cmmd END','func',4,'p_func','semtic.py',142),
  ('func -> DEF ID LPAREN objs RPAREN cmmd RETURN obj END','func',9,'p_func','semtic.py',143),
  ('func -> DEF ID LPAREN RPAREN cmmd RETURN obj END','func',8,'p_func','semtic.py',144),
  ('func -> DEF ID cmmd RETURN obj END','func',6,'p_func','semtic.py',145),
  ('else -> ELSE comptn cmmd','else',3,'p_else','semtic.py',150),
  ('else -> ELSE bool cmmd','else',3,'p_else','semtic.py',151),
  ('elsif -> ELSIF comptn cmmd','elsif',3,'p_elsif','semtic.py',156),
  ('elsif -> ELSIF bool cmmd','elsif',3,'p_elsif','semtic.py',157),
  ('elses -> else','elses',1,'p_elses','semtic.py',162),
  ('elses -> elsif elses','elses',2,'p_elses','semtic.py',163),
  ('control -> IF comptn cmmd END','control',4,'p_contol_if','semtic.py',168),
  ('control -> IF bool cmmd END','control',4,'p_contol_if','semtic.py',169),
  ('control -> IF comptn cmmd elses END','control',5,'p_contol_if','semtic.py',170),
  ('control -> IF bool cmmd elses END','control',5,'p_contol_if','semtic.py',171),
  ('control -> UNLESS comptn COLON cmmd END','control',5,'p_control_unless','semtic.py',176),
  ('control -> UNLESS bool COLON cmmd END','control',5,'p_control_unless','semtic.py',177),
  ('control -> UNLESS comptn cmmd elses END','control',5,'p_control_unless','semtic.py',178),
  ('control -> UNLESS bool cmmd elses END','control',5,'p_control_unless','semtic.py',179),
  ('control -> CASE ID whens else END','control',5,'p_control_case','semtic.py',184),
  ('control -> CASE ID whens END','control',4,'p_control_case','semtic.py',185),
  ('control -> WHILE comptn DO cmmd END','control',5,'p_control_while','semtic.py',190),
  ('control -> WHILE bool DO cmmd END','control',5,'p_control_while','semtic.py',191),
  ('when -> WHEN objs','when',2,'p_when','semtic.py',196),
  ('when -> WHEN objs THEN','when',3,'p_when','semtic.py',197),
  ('when -> WHEN comptn','when',2,'p_when','semtic.py',198),
  ('whens -> when','whens',1,'p_whens','semtic.py',203),
  ('whens -> when whens','whens',2,'p_whens','semtic.py',204),
  ('ids -> ID','ids',1,'p_ids','semtic.py',209),
  ('ids -> ID COMMA ids','ids',3,'p_ids','semtic.py',210),
  ('array -> LBRAKET objs RBRAKET','array',3,'p_array','semtic.py',215),
  ('array -> LBRAKET ids RBRAKET','array',3,'p_array','semtic.py',216),
  ('array -> LBRAKET objs COMMA ids RBRAKET','array',5,'p_array','semtic.py',217),
  ('array -> LBRAKET ids COMMA objs RBRAKET','array',5,'p_array','semtic.py',218),
  ('arrays -> array','arrays',1,'p_arrays','semtic.py',223),
  ('arrays -> array COMMA arrays','arrays',3,'p_arrays','semtic.py',224),
  ('strucMatrix -> MATRIX LBRAKET arrays RBRAKET','strucMatrix',4,'p_strucMatrix','semtic.py',229),
  ('strucSet -> SET DOT NEW','strucSet',3,'p_strucSet','semtic.py',233),
  ('strucSet -> SET DOT NEW LPAREN RPAREN','strucSet',5,'p_strucSet','semtic.py',234),
  ('strucSet -> SET DOT NEW LPAREN array RPAREN','strucSet',6,'p_strucSet','semtic.py',235),
  ('strucSet -> SET array','strucSet',2,'p_strucSet','semtic.py',236),
  ('strucHash -> HASH DOT NEW','strucHash',3,'p_strucHash','semtic.py',241),
  ('strucHash -> HASH DOT NEW LBRACE RBRACE','strucHash',5,'p_strucHash','semtic.py',242),
  ('strucHash -> HASH DOT NEW LBRACE hashelems RBRACE','strucHash',6,'p_strucHash','semtic.py',243),
  ('strucHash -> HASH array','strucHash',2,'p_strucHash','semtic.py',244),
  ('hashelem -> COLON ID ROCKET obj','hashelem',4,'p_hashelem_rocket','semtic.py',249),
  ('hashelem -> ID COLON obj','hashelem',3,'p_hashelem_json','semtic.py',253),
  ('hashelem -> STRING COLON obj','hashelem',3,'p_hashelem_string','semtic.py',257),
  ('hashelems -> hashelem COMMA hashelem','hashelems',3,'p_hashelems','semtic.py',261),
  ('hashelems -> hashelem COMMA hashelems','hashelems',3,'p_hashelems','semtic.py',262),
  ('objs -> obj','objs',1,'p_objs','semtic.py',267),
  ('objs -> obj COMMA objs','objs',3,'p_objs','semtic.py',268),
  ('obj -> STRING','obj',1,'p_obj','semtic.py',273),
  ('obj -> num','obj',1,'p_obj','semtic.py',274),
  ('obj -> bool','obj',1,'p_obj','semtic.py',275),
  ('obj -> range','obj',1,'p_obj','semtic.py',276),
  ('struc -> strucMatrix','struc',1,'p_struc','semtic.py',281),
  ('struc -> strucSet','struc',1,'p_struc','semtic.py',282),
  ('struc -> strucHash','struc',1,'p_struc','semtic.py',283),
  ('range -> LPAREN INT DOT DOT INT RPAREN','range',6,'p_range','semtic.py',288),
  ('range -> INT DOT DOT INT','range',4,'p_range','semtic.py',289),
  ('range -> LPAREN STRING DOT DOT STRING','range',5,'p_range','semtic.py',290),
  ('range -> STRING DOT DOT STRING','range',4,'p_range','semtic.py',291),
  ('cmmd -> var','cmmd',1,'p_cmmd','semtic.py',296),
  ('cmmd -> func','cmmd',1,'p_cmmd','semtic.py',297),
  ('cmmd -> control','cmmd',1,'p_cmmd','semtic.py',298),
  ('cmmd -> optns','cmmd',1,'p_cmmd','semtic.py',299),
]
