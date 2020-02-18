class gamestate(): 
    #This file is a persistent constructor for the gamestate such as who's turn, a numerical representation etc.
    def __init__(self, board_size, gameMatrix):
            self.board_size = board_size
            self.isBlackTurn = True
            self.isCheck = False
            self.gameState = 0
            self.newMatrixPosX = None
            self.newMatrixPosY = None
            self.oldMatrixPosX = None
            self.oldMatrixPosY = None
            self.pieceSelected = None
            self.possibleMoveMatrix = []
            self.gameMatrix = gameMatrix
            self.blackcaptured = []
            self.whitecaptured = []
            self.droprank = 0
            self.isLoad = False
            self.isAI = False
            self.recordingFile = ''
            self.loadFile = ''
            self.playerSelected = None
            self.autoPlay = None
            self.NumericalEncodingGameState = None
            self.dropBlackPcs = None
            self.dropWhitePcs = None
            self.AIMessage = ''
            self.isPromotionMessageActive = False