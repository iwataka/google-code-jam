import           Control.Monad

data Move = East|South deriving (Eq, Show)

main = do
    nTests <- readLn
    forM [1..nTests] $ \i -> do
        w' <- getLine
        let w = read w' :: Int
        ms <- getLine
        let ans = solve ms w
        putStrLn $ "Case #" ++ (show i) ++ ": " ++ ans

toMove :: Char -> Move
toMove m = case m of
    'E' -> East
    'S' -> South
    _   -> error $ "Invalid character: " ++ (show m)

moveToStr m = case m of
    East  -> "E"
    South -> "S"

invMove m = case m of
    East  -> South
    South -> East

untilConsecutiveMove ms m
    | m1 == m2 && m1 == m = []
    | otherwise = m1 : (untilConsecutiveMove (m2:rest) m)
    where
        m1:m2:rest = ms

solve' ms w
    | h /= l =
        replicate (w - 1) l ++ (replicate (w - 1) h)
    | otherwise = do
        let iniMove = invMove h
            msUntilConsecutiveMoves = untilConsecutiveMove ms iniMove
            straightCount = length $ filter (== iniMove) msUntilConsecutiveMoves
            firstMoves = iniMove : replicate straightCount iniMove
            secondMoves = replicate (w - 1) h
            thirdMoves = replicate (w - straightCount - 2) iniMove
        firstMoves ++ secondMoves ++ thirdMoves
    where
        h = head ms
        l = last ms

solve :: [Char] -> Int -> [Char]
solve ms' w = do
    let ms = map toMove ms'
    let ans = solve' ms w
    concat $ map moveToStr ans
