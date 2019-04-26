class QueueNode {
    int row;
    int data;

    QueueNode(int row, int data) {
        this.row = row;
        this.data = data;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if( !(other instanceof QueueNode)) return false;

        QueueNode node = (QueueNode)other;
        return node.data == this.data &&
                node.row == this.row;
    }

    @Override
    public int hashCode() {
        int result = 17;
        result = 31 * result + this.row;
        result = 31 * result + this.data;
        return result;
    }

    @Override
    public String toString() {
        return "\n"+"row: "+this.row+"\t"+"data: "+this.data+"\n";
    }
}

class PQ {
    private QueueNode[] nodes;
    private int capacity;
    private int position;

    public PQ(int capacity) {
        this.capacity = capacity;
        this.position = 0;
        nodes = new QueueNode[this.capacity];
    }

    void add(QueueNode node) {
        if (this.position == 0) {
            this.nodes[this.position] = node;
            this.position = 1;
        } else {
            this.nodes[this.position++] = node;
            this.bubbleUp();
        }
    }

    void bubbleUp() {
        int pos = this.position - 1;
        while(pos >= 0 && this.nodes[pos].data < this.nodes[pos/2].data) {
            swap(pos, pos/2);
            pos = pos/2;
        }
    }

    QueueNode extractMin() {
        QueueNode minNode = this.nodes[0];
        this.nodes[0] = this.nodes[this.position-1];
        this.nodes[this.position-1] = null;
        this.position -= 1;
        shrink(0);
        return minNode;
    }

    void shrink(int pos) {
        int left = (2*pos)+1;
        int right = (2*pos) + 2;
        int smallest = pos;

        if(left < this.position && this.nodes[left].data <= this.nodes[smallest].data) {
            smallest = left;
        }

        if (right < this.position && this.nodes[right].data <= this.nodes[smallest].data) {
            smallest = right;
        }

        if (smallest != pos) {
            swap(smallest, pos);
            shrink(smallest);
        }
    }

    void swap(int left, int right) {
        QueueNode temp = this.nodes[left];
        this.nodes[left] = this.nodes[right];
        this.nodes[right] = temp;
    }

    boolean isEmpty() {
        return this.position == 0;
    }
}

class Prim {
    public void prim(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int size = row*col;

        QueueNode[] arrays = new QueueNode[row];
        for(int i=0; i<row; i++) {
            arrays[i] = new QueueNode(i, i==0?0:Integer.MAX_VALUE);
        }

        int[] parent = new int[row];
        boolean[] visited = new boolean[row];

        PQ pq = new PQ(size);
        QueueNode start = new QueueNode(0, matrix[0][0]);
        pq.add(start);

        while(!pq.isEmpty()) {
            QueueNode temp = pq.extractMin();

            int k = temp.row;
            for(int i=0; i<matrix[k].length;i++) {
                int value = matrix[k][i];
                if (value != 0 && value < arrays[i].data && !visited[i]) {
                    arrays[i].data = value;
                    arrays[i].row = i;
                    pq.add(arrays[i]);
                    parent[i] = k;
                }
            }
            visited[k]= true;
        }
        printMST(parent, matrix);
    }

    void printMST(int[] parent, int[][] matrix) {
        for(int i=1; i<matrix.length; i++) {
            System.out.println(parent[i]+" - "+ i+"\t"+ matrix[i][parent[i]]);
        }
    }
}

public class Main {
    public static void main(String[] args)
    {
        System.out.println("Hello World!");
        int[][] matrix = {
                {0,19,0,14,12,0,0,0,0,0},
                {19,0,20,0,18,0,0,0,0,0},
                {0,20,0,0,17,15,0,0,0,29},
                {14,0,0,0,13,0,28,0,0,0},
                {12,18,17,13,0,16,21,22,24,0},
                {0,0,15,0,16,0,0,0,26,27},
                {0,0,0,28,21,0,0,23,0,0},
                {0,0,0,0,22,0,23,0,30,0},
                {0,0,0,0,24,26,0,30,0,35},
                {0,0,0,0,24,26,0,30,35,0}
        };

        Prim p = new Prim();
        p.prim(matrix);
    }